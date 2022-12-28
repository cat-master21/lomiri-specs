%global source_date_epoch_from_changelog 0

Name:          lomiri-api
Version:       0.1.1
Release:       1%{?dist}
Summary:       API for Lomiri

License:       LGPLv3+
URL:           https://gitlab.com/ubports/development/core/lomiri-api
Source0:       %{url}/-/archive/%{version}/lomiri-api-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: doxygen

%description
API to interface with the Lomiri desktop environment.

%package devel
Summary:  API library for Lomiri
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for Lomiri API.

%package doc
Summary: Documenation for %{name}
BuildArch: noarch

%description doc
The %{name}-doc contains documentation for %{name}.

%prep
%setup -q -n lomiri-api-%{version}

%build
# Requires static file that Fedora doesn't package
sed -i 's/add_subdirectory(gtest)//' test/CMakeLists.txt
# Hard-coded for Debians' libdir
sed -i 's?lib/${CMAKE_LIBRARY_ARCHITECTURE}?%{_lib}?' CMakeLists.txt
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/liblomiri-api.so.*

%files devel
%license COPYING
%{_libdir}/liblomiri-api.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/lomiri
%{_includedir}/lomiri/*.h
%dir %{_includedir}/lomiri/api
%{_includedir}/lomiri/api/*.h
%dir %{_includedir}/lomiri/shell
%dir %{_includedir}/lomiri/shell/application
%{_includedir}/lomiri/shell/application/*.h
%dir %{_includedir}/lomiri/shell/launcher
%{_includedir}/lomiri/shell/launcher/*.h
%dir %{_includedir}/lomiri/shell/notifications
%{_includedir}/lomiri/shell/notifications/*.h
%dir %{_includedir}/lomiri/util
%{_includedir}/lomiri/util/*.h

%files doc
%{_docdir}/liblomiri-api/
