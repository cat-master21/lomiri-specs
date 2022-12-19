%global source_date_epoch_from_changelog 0

Name:           qtmir
Version:        0.7.0
Release:        1
Summary:        Mir backed compositor using Qt

License:        LGPLv3+ AND GPLv3+
URL:            https://gitlab.com/ubports/development/core/qtmir
Source0:        %{url}/-/archive/main/qtmir-main.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Sensors)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(mirserver)
BuildRequires: pkgconfig(mirclient)
BuildRequires: pkgconfig(mir-renderer-gl-dev)
BuildRequires: pkgconfig(miral)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(process-cpp)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(lomiri-url-dispatcher)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: pkgconfig(lomiri-shell-application)
BuildRequires: pkgconfig(libcontent-hub)

%description
Mir backed compositor using QT which is used for Lomiri.


%package devel
Summary:  Qtmir development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for qtmir.

%package demo
Summary: Qtmir demos
Requires: %{name}%{?_isa} = %{version}-%{release}

%description demo
This package contains development files needed for qtmir.

%prep
%setup -q -n qtmir-main

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%license COPYING COPYING.LESSER
%{_libdir}/libqtmirserver.so.*
%{_qt5_plugindir}/platforms/libqpa-mirserver.so
%dir %{_qt5_qmldir}/QtMir
%dir %{_qt5_qmldir}/QtMir/Application
%{_qt5_qmldir}/QtMir/Application/libqtmirapplicationplugin.so
%{_qt5_qmldir}/QtMir/Application/qmldir
%{_datadir}/glib-2.0/schemas/com.canonical.qtmir.gschema.xml

%files devel
%license COPYING COPYING.LESSER
%{_libdir}/libqtmirserver.so
%{_libdir}/pkgconfig/qtmirserver.pc
%dir %{_includedir}/qtmir
%dir %{_includedir}/qtmir/qtmir
%{_includedir}/qtmir/qtmir/*.h
%dir %{_includedir}/qtmir/qtmir/miral
%{_includedir}/qtmir/qtmir/miral/*.h

%files demo
%license COPYING COPYING.LESSER
%{_bindir}/qtmir-demo-*
%{_datadir}/applications/qtmir-demo-client.desktop
%dir %{_datadir}/qtmir
%dir %{_datadir}/qtmir/benchmarks
%{_datadir}/qtmir/benchmarks/*.py
%{_datadir}/qtmir/benchmarks/*.R
%dir %{_datadir}/qtmir/qtmir-demo-client
%{_datadir}/qtmir/qtmir-demo-client/*.qml
%dir %{_datadir}/qtmir/qtmir-demo-shell
%{_datadir}/qtmir/qtmir-demo-shell/*.qml
%{_datadir}/qtmir/qtmir-demo-shell/*.png
