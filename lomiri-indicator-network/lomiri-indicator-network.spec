%global source_date_epoch_from_changelog 0

Name:       lomiri-indicator-network
Version:    16.10.0
Release:    1%{?dist}
Summary:    The Network indicator for Ubuntu Touch
License:    GPLv3 AND LGPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-indicator-network
Source0:    %{url}/-/archive/main/lomiri-indicator-network-main.tar.gz

BuildRequires: systemd-rpm-macros
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(ofono)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: pkgconfig(libgmenuharness)
BuildRequires: pkgconfig(ofono)
BuildRequires: pkgconfig(qofono-qt5)
BuildRequires: pkgconfig(lomiri-url-dispatcher)

%description
The "Network" indicator for Ubuntu Touch and Lomiri.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%autosetup -n lomiri-indicator-network-main

%build
%cmake -DENABLE_COVERAGE=OFF -DENABLE_UBUNTU_COMPAT=ON
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYING.LGPL
%{_sysconfdir}/xdg/autostart/lomiri-indicator-network.desktop
%{_userunitdir}/*.service
%{_libdir}/liblomiri-connectivity-qt1.so.*
%dir %{_qt5_qmldir}/Lomiri/Connectivity
%{_qt5_qmldir}/Lomiri/Connectivity/libconnectivity-qml.so
%{_qt5_qmldir}/Lomiri/Connectivity/qmldir
%dir %{_qt5_qmldir}/Ubuntu/Connectivity
%{_qt5_qmldir}/Ubuntu/Connectivity/libconnectivity-qml-ubuntu-compat.so
%{_qt5_qmldir}/Ubuntu/Connectivity/qmldir
%dir %{_libexecdir}/lomiri-indicator-network
%{_libexecdir}/lomiri-indicator-network/lomiri-indicator-network-*
%{_datadir}/glib-2.0/schemas/com.lomiri.indicator.network.gschema.xml
%{_datadir}/unity/indicators/com.lomiri.indicator.network

%files devel
%license COPYING COPYING.LGPL
%dir %{_includedir}/connectivity-api
%dir %{_includedir}/connectivity-api/qt1
%dir %{_includedir}/connectivity-api/qt1/connectivityqt
%{_includedir}/connectivity-api/qt1/connectivityqt/*.h
%dir %{_includedir}/connectivity-api/qt1/lomiri
%dir %{_includedir}/connectivity-api/qt1/lomiri/connectivity
%{_includedir}/connectivity-api/qt1/lomiri/connectivity/networking-status.h
%{_libdir}/liblomiri-connectivity-qt1.so
%{_libdir}/pkgconfig/lomiri-connectivity-qt1.pc

%files doc
%dir %{_docdir}/lomiri-connectivity-doc
%{_docdir}/lomiri-connectivity-doc/cpp/
%{_docdir}/lomiri-connectivity-doc/dbus/
%{_docdir}/lomiri-connectivity-doc/qml/
