%global source_date_epoch_from_changelog 0

Name:       content-hub
Version:    1.0
Release:    1%{?dist}
Summary:    Content sharing/picking service
License:    GPLv3 AND LGPLv3
URL:        https://gitlab.com/ubports/development/core/content-hub
Source0:    %{url}/-/archive/main/content-hub-main.tar.gz

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: qt5-mobility-feedback-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtgraphicaleffects
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(lomiri-download-manager-client)

%description
content sharing/picking service
Content sharing/picking infrastructure and service, designed to allow apps to
securely and efficiently exchange content.
This package includes the content sharing service.
content sharing/picking library
Content sharing/picking infrastructure and service, designed to allow apps to
securely and efficiently exchange content.
This package includes the content sharing libraries.
content sharing/picking library - GLib bindings
Content sharing/picking infrastructure and service, designed to allow apps to
securely and efficiently exchange content.
.
This package includes GLib bindings of the content sharing libraries.
QML binding for libcontent-hub
QML bindings for libcontent-hub
Documentation files for libcontent-hub-dev
Documentation files for the libcontent-hub development
content sharing testability
Files and utilities needed for automated testing of content-hub

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications for use with %{name}.

%package testability
Summary: Tests for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description testability
Test files and apparmor profile for %{name}.

%package doc
Summary: Documentation for %{name}-devel
BuildArch: noarch

%description doc
Documentation files for %{name}-devel.

%prep
%autosetup -p1 -n content-hub-main
sed -i 's/ -qt=qt5//' import/Lomiri/Content/CMakeLists.txt
sed -i 's/ -qt=qt5//' doc/qml/CMakeLists.txt
sed -i 'sXqmlplugindumpX%{_qt5_bindir}/qmlplugindumpX' import/Lomiri/Content/CMakeLists.txt

%build
%cmake -DENABLE_TESTS=ON -DENABLE_DOC=ON -DENABLE_UBUNTU_COMPAT=ON
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/etc/apparmor.d
cp debian/apparmor/content-hub-testability %{buildroot}/etc/apparmor.d
%find_lang %{name}

%files -f %{name}.lang
%license COPYING.GPL COPYING.LGPL
%{_bindir}/content-hub-send
%{_bindir}/content-hub-service
%{_libdir}/libcontent-hub.so.*
%{_libdir}/libcontent-hub-glib.so.*
%{_qt5_qmldir}/Lomiri/Content/
%{_qt5_qmldir}/Ubuntu/Content/
%{_datadir}/applications/content-hub-send.desktop
%dir %{_datadir}/content-hub
%{_datadir}/content-hub/icons/
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/lomiri-url-dispatcher/urls/*.url-dispatcher

%files devel
%license COPYING.GPL COPYING.LGPL
%{_libdir}/libcontent-hub.so
%{_libdir}/libcontent-hub-glib.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/com
%dir %{_includedir}/com/lomiri
%dir %{_includedir}/com/lomiri/content
%{_includedir}/com/lomiri/content/*.h
%dir %{_includedir}/com/lomiri/content/glib
%{_includedir}/com/lomiri/content/glib/*.h

%files testability
%license COPYING.GPL COPYING.LGPL
%{_sysconfdir}/apparmor.d/content-hub-testability
%{_bindir}/content-hub-test*
%{_datadir}/applications/content-hub-test-*.desktop
%{_datadir}/content-hub/peers/
%{_datadir}/content-hub/testability/
%{_datadir}/icons/hicolor/512x512/apps/*.png

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/cpp/
%{_docdir}/%{name}/qml/
