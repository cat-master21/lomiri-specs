%global source_date_epoch_from_changelog 0

Name:          lomiri-api
Version:       0.1.1
Release:       1
Summary:       API for Lomiri

License:       LGPLv3+
URL:           https://gitlab.com/ubports/core/lomiri-api
Source0:       %{url}/-/archive/%{version}/lomiri-api-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)

%description
API to interface with the Lomiri desktop environment.


%package devel
Summary:  API library for Lomiri
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for Lomiri API.


%prep
%setup -q -n lomiri-api-%{version}

%build
sed -i 's/add_subdirectory(gtest)//' test/CMakeLists.txt
%cmake

%cmake_build

%install
%cmake_install
# The libraries are still 64-bit if on 64-bit machine so they should be moved if necessary
if [ %{_lib} == lib64 ]
then
mv -f %{buildroot}%{_prefix}/lib/*.* %{buildroot}%{_libdir}
mv -f %{buildroot}%{_prefix}/lib/pkgconfig/* %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_prefix}/lib
fi

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
