%global source_date_epoch_from_changelog 0

Name:          lomiri
Version:       0.1
Release:       1%{?dist}
Summary:       A convergent desktop environment

License:       GPLv3 AND LGPLv3
URL:           https://gitlab.com/ubports/development/core/lomiri
Source0:       %{url}/-/archive/main/lomiri-main.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
#BuildRequires: doxygen
#BuildRequires: doxyqml
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(lomiri-shell-application)
BuildRequires: pkgconfig(qtmirserver)
BuildRequires: pkgconfig(geonames)
BuildRequires: pkgconfig(lomiri-shell-launcher)
BuildRequires: pkgconfig(qmenumodel)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(LomiriGestures)
BuildRequires: pkgconfig(miral)
BuildRequires: pkgconfig(deviceinfo)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: pkgconfig(LomiriSystemSettings)
BuildRequires: pkgconfig(liblightdm-qt5-3)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(libusermetricsoutput-1)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: dpkg-dev
BuildRequires: systemd-rpm-macros
Recommends:    lomiri-system-compositor
Recommends:    lomiri-desktop-session
Requires:      xorg-x11-server-Xwayland
Requires:      ayatana-indicator-datetime
Requires:      lomiri-sounds
Requires:      lomiri-keyboard
Requires:      lomiri-ui-toolkit
Requires:      lomiri-download-manager
Requires:      suru-icon-theme
Requires:      lomiri-schemas

%description
Lomiri, Previously Unity8 is a convergent desktop environment built with Qt.

# Documentation needs doxyqml
#package doc
#Summary: Documentation files for {name}
#BuildArch: noarch

#description doc
#The {name}-doc package contains documenation files for {name}.

%package tests
Summary: Test files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains test files for %{name}.

%prep
%autosetup -n lomiri-main

%build
%cmake -DWerror=OFF -DDEB_HOST_MULTIARCH=%{_arch} -DCMAKE_INSTALL_LOCALSTATEDIR="%{_localstatedir}"
%cmake_build

%install
%cmake_install
#cd tests/autopilot && python setup.py install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYING.LGPL
%{_bindir}/indicators-client
%{_bindir}/lomiri
%{_userunitdir}/*.service
%{_libdir}/liblomiri-private.so*
%dir %{_libdir}/lomiri
%dir %{_libdir}/lomiri/qml
%{_libdir}/lomiri/qml/AccountsService/
%{_libdir}/lomiri/qml/Cursor/
%{_libdir}/lomiri/qml/GlobalShortcut/
%{_libdir}/lomiri/qml/Greeter/
%{_libdir}/lomiri/qml/LightDM/
%{_libdir}/lomiri/qml/Lomiri/
%{_libdir}/lomiri/qml/Powerd/
%{_libdir}/lomiri/qml/ScreenshotDirectory/
%{_libdir}/lomiri/qml/SessionBroadcast/
%{_libdir}/lomiri/qml/UInput/
%{_libdir}/lomiri/qml/Utils/
%{_libdir}/lomiri/qml/WindowManager/
%{_libdir}/lomiri/qml/Wizard/
%{_libexecdir}/lomiri-systemd-wrapper
%{_datadir}/accountsservice/interfaces/com.lomiri.shell.AccountsService.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/interfaces/com.lomiri.shell.AccountsService.xml
%{_datadir}/lightdm/greeters/lomiri-greeter.desktop
%{_datadir}/lightdm/lightdm.conf.d/51-lomiri-greeter.conf
%dir %{_datadir}/lomiri
%{_datadir}/lomiri/unlock-device
%{_datadir}/lomiri/qmldir
%{_datadir}/lomiri/*.qml
%{_datadir}/lomiri/ApplicationMenus/
%{_datadir}/lomiri/Components/
%{_datadir}/lomiri/Notifications/
%{_datadir}/lomiri/Stage/
%{_datadir}/lomiri/Panel/
%{_datadir}/lomiri/Tutorial/
%{_datadir}/lomiri/graphics/
%{_datadir}/lomiri/Rotation/
%{_datadir}/lomiri/Greeter/
%{_datadir}/lomiri/Wizard/
%{_datadir}/lomiri/Launcher/
%dir %{_sharedstatedir}/lomiri
%{_sharedstatedir}/lomiri/version
%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/50-com.lomiri.wizard.pkla

%files tests
%license COPYING COPYING.LGPL
%{_bindir}/lomiri-mock-indicator-service
%{_libdir}/lomiri/qml/mocks/
%{_libdir}/lomiri/qml/nonmirplugins/
%{_libdir}/lomiri/qml/utils/
%dir %{_libexecdir}/lomiri
%{_libexecdir}/lomiri/uqmlscene
%dir %{_libexecdir}/lomiri/tests
%{_libexecdir}/lomiri/tests/plugins/
%{_libexecdir}/lomiri/tests/qmltests/
%{_libexecdir}/lomiri/tests/scripts/
%{_datadir}/lomiri/mocks/
%{_datadir}/lomiri/tests/
