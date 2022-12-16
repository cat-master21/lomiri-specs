%global source_date_epoch_from_changelog 0

Name:       lomiri-download-manager
Version:    1.1
Release:    1%{?dist}
Summary:    Upload Download Manager for Lomiri
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-download-manager
Source0:    %{url}/-/archive/main/lomiri-download-manager-main.tar.gz

BuildRequires: systemd-rpm-macros
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-doctools
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pkgconfig(dbus-1)

%description
Upload Download Manager - shared common library
Upload Download Manager performs uploads and downloads from a centralized
location.
.
This package includes the common shared library between the client lib and the
service lib.
Ubuntu Download Manager - shared common library
Ubuntu Download Manager performs downloads from a centralized location.
.
This package includes the common shared library between the client lib and the
service lib.
Ubuntu Download Manager - shared public library
Ubuntu Download Manager performs downloads from a centralized location.
.
This package includes the public shared library.

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
%{name}-doc contains documentation for %{name}-devel.

%prep
%autosetup -p1 -n lomiri-download-manager-main
sed -e "s/-Werror//g" -i CMakeLists.txt
sed -i 's/ -qt=qt5//' docs/qml/CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_LIBEXECDIR=%{_libdir} -DENABLE_UBUNTU_COMPAT=ON
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_sysconfdir}/dbus-1/system.d/*.conf
%{_bindir}/lomiri-*
%{_userunitdir}/*.service
%{_libdir}/liblomiri-download-manager-client.so.*
%{_libdir}/liblomiri-download-manager-common.so.*
%{_libdir}/liblomiri-upload-manager-common.so.*
%{_libdir}/libldm-common.so.*
%{_libdir}/libldm-priv-common.so.*
%dir %{_libdir}/lomiri-download-manager
%{_libdir}/lomiri-download-manager/ldm-extractor
%{_qt5_qmldir}/Lomiri/
%{_qt5_qmldir}/Ubuntu/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service

%files devel
%license COPYING
%dir %{_includedir}/lomiri/download_manager
%{_includedir}/lomiri/download_manager/*.h
%dir %{_includedir}/lomiri/transfers
%{_includedir}/lomiri/transfers/*.h
%dir %{_includedir}/lomiri/transfers/errors
%{_includedir}/lomiri/transfers/errors/*.h
%dir %{_includedir}/lomiri/upload_manager
%{_includedir}/lomiri/upload_manager/*.h
%{_libdir}/liblomiri-download-manager-client.so
%{_libdir}/liblomiri-download-manager-common.so
%{_libdir}/liblomiri-upload-manager-common.so
%{_libdir}/libldm-common.so
%{_libdir}/libldm-priv-common.so
%{_libdir}/pkgconfig/*.pc

%files doc
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/cpp
%{_docdir}/%{name}/cpp/html/
%dir %{_docdir}/%{name}/qml
%{_docdir}/%{name}/qml/html/
