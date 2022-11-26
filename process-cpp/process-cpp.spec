%global source_date_epoch_from_changelog 0

Name:           process-cpp
Version:        3.0.1
Release:        1%{?dist}
Summary:        A simple convenience library for handling processes in C++11

License:        LGPLv3+
URL:            https://gitlab.com/ubports/development/core/lib-cpp/process-cpp
Source0:        %{url}/-/archive/main/process-cpp-main.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: doxygen


%description
A simple convenience library for handling processes in C++11.

%package devel
Summary:  process-cpp development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for process-cpp.

%package doc
Summary:   process-cpp documentation files
BuildArch: noarch

%description doc
This package contains documentation files for process-cpp.


%prep
%setup -q -n process-cpp-main

%build
sed -i '/add_subdirectory(tests)/d' ./CMakeLists.txt
%cmake -DPROCESS_CPP_WERROR=OFF

%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/libprocess-cpp.so.*


%files devel
%{_libdir}/libprocess-cpp.so
%{_libdir}/pkgconfig/process-cpp.pc
%dir %{_includedir}/core/testing
%{_includedir}/core/testing/*.h
%dir %{_includedir}/core/posix
%{_includedir}/core/posix/*.h
%dir %{_includedir}/core/posix/linux
%dir %{_includedir}/core/posix/linux/proc
%dir %{_includedir}/core/posix/linux/proc/process
%{_includedir}/core/posix/linux/proc/process/*.h


%files doc
%license COPYING
%dir %{_docdir}/process-cpp
%dir %{_docdir}/process-cpp/html
%{_docdir}/process-cpp/html/*.html
%{_docdir}/process-cpp/html/*.map
%{_docdir}/process-cpp/html/*.css
%{_docdir}/process-cpp/html/*.png
%{_docdir}/process-cpp/html/*.js
%{_docdir}/process-cpp/html/*.md5
%{_docdir}/process-cpp/html/*.svg
