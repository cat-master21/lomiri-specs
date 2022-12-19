%global source_date_epoch_from_changelog 0

Name:       deviceinfo
Version:    0.1.0
Release:    1%{?dist}
Summary:    Library to detect and configure devices
License:    GPLv3
URL:        https://gitlab.com/ubports/development/core/deviceinfo
Source0:    %{url}/-/archive/main/deviceinfo-main.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++

%description
Library to detect and configure devices for Lomiri.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n deviceinfo-main

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%dir %{_sysconfdir}/deviceinfo
%{_sysconfdir}/deviceinfo/default.yaml
%dir %{_sysconfdir}/deviceinfo/devices
%{_sysconfdir}/deviceinfo/devices/*.yaml
%dir %{_sysconfdir}/deviceinfo/sensorfw
%{_sysconfdir}/deviceinfo/sensorfw/*.conf
%{_bindir}/device-info
%{_libdir}/libdeviceinfo.so.*

%files devel
%license LICENSE
%dir %{_includedir}/deviceinfo
%{_includedir}/deviceinfo/deviceinfo.h
%{_libdir}/libdeviceinfo.so
%{_libdir}/pkgconfig/deviceinfo.pc
