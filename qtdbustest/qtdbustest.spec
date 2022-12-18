%global source_date_epoch_from_changelog 0

Name:       qtdbustest
Version:    0.2
Release:    1%{?dist}
Summary:    Library for testing DBus interactions using Qt5
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/packaging/libqtdbustest
Source0:    %{url}/-/archive/ubports/xenial/libqtdbustest-ubports-xenial.tar.gz
Source1:    %{url}/-/archive/ubports/latest/libqtdbustest-ubports-latest.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcovr
BuildRequires: lcov
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)

Requires: %{name}%{?_isa} = %{version}-%{release}
%description
Library for testing DBus interactions using Qt
A simple library for testing Qt based DBus services and clients.
This package contains the shared libraries.

%package devel
Summary: Development files for %{name}

%description devel
%{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n libqtdbustest-ubports-xenial
tar -xf '%{SOURCE1}'
for i in libqtdbustest-ubports-latest/debian/patches/*.patch; do patch -p1 < $i; done

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_bindir}/qdbus-simple-test-runner
%{_libdir}/libqtdbustest.so.*
%dir %{_libexecdir}/libqtdbustest
%{_libexecdir}/libqtdbustest/watchdog
%dir %{_datadir}/libqtdbustest
%{_datadir}/libqtdbustest/*.conf

%files devel
%license COPYING
%dir %{_includedir}/libqtdbustest-1
%dir %{_includedir}/libqtdbustest-1/libqtdbustest
%{_includedir}/libqtdbustest-1/libqtdbustest/*.h
%{_libdir}/libqtdbustest.so
%{_libdir}/pkgconfig/libqtdbustest-1.pc
