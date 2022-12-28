%global source_date_epoch_from_changelog 0

Name:       qtdbusmock
Version:    0.7
Release:    1%{?dist}
Summary:    Library for mocking DBus interactions using Qt
License:    LGPLv3
URL:        https://github.com/ubports/libqtdbusmock
Source0:    %{url}/archive/refs/heads/xenial.tar.gz
Patch0:     https://salsa.debian.org/debian-ayatana-team/libqtdbusmock/-/raw/master/debian/patches/1001_port-to-libnm.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)

%description
Library for mocking DBus interactions using Qt
A simple library for mocking DBus services with a Qt API.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n libqtdbusmock-xenial
# Revert this so the patch can be applied with other fixes
sed -i 's/libnm/NetworkManager/' CMakeLists.txt 
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/libqtdbusmock.so.*
%dir %{_datadir}/libqtdbusmock
%dir %{_datadir}/libqtdbusmock/templates
%{_datadir}/libqtdbusmock/templates/*.py

%files devel
%license COPYING
%dir %{_includedir}/libqtdbusmock-1
%dir %{_includedir}/libqtdbusmock-1/libqtdbusmock
%{_includedir}/libqtdbusmock-1/libqtdbusmock/*.h
%{_libdir}/libqtdbusmock.so
%{_libdir}/pkgconfig/libqtdbusmock-1.pc
