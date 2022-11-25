%global source_date_epoch_from_changelog 0

Name:           properties-cpp-devel
Version:        0.0.2
Release:        1%{?dist}
Summary:        A very simple convenience library for handling properties and signals in C++11

License:        LGPLv3+
URL:            https://gitlab.com/ubports/development/core/lib-cpp/properties-cpp
Source0:        %{url}/-/archive/main/properties-cpp-main.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: doxygen


%description
A very simple convenience library for handling properties and signals in C++11.


%package doc
Summary:  properties-cpp development files
BuildArch: noarch

%description doc
This package contains documentation files for properties-cpp-devel.


%prep
%setup -q -n properties-cpp-main

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/pkgconfig/properties-cpp.pc
%{_includedir}/core/*.h


%files doc
%license COPYING
%dir %{_docdir}/properties-cpp
%dir %{_docdir}/properties-cpp/html
%{_docdir}/properties-cpp/html/*.html
%{_docdir}/properties-cpp/html/*.map
%{_docdir}/properties-cpp/html/*.css
%{_docdir}/properties-cpp/html/*.png
%{_docdir}/properties-cpp/html/*.js
%{_docdir}/properties-cpp/html/*.md5
%{_docdir}/properties-cpp/html/*.svg
