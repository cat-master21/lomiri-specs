%global source_date_epoch_from_changelog 0

Name:       geonames
Version:    0.3.0
Release:    1%{?dist}
Summary:    Parse and query the geonames database
License:    GPLv3
URL:        https://gitlab.com/ubports/development/core/geonames
Source0:    %{url}/-/archive/main/geonames-main.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libtool

%description
A library for parsing and querying a local copy of the geonames.org database.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
The %{name}-doc package contains documenation for %{name}.

%prep
%autosetup -n geonames-main

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYING.data
%{_libdir}/libgeonames.so.*

%files devel
%license COPYING
%dir %{_includedir}/geonames
%{_includedir}/geonames/geonames.h
%{_libdir}/libgeonames.so
%{_libdir}/pkgconfig/geonames.pc

%files doc
%license COPYING
%dir %{_datadir}/gtk-doc/html/geonames
%{_datadir}/gtk-doc/html/geonames/*.html
%{_datadir}/gtk-doc/html/geonames/*.png
%{_datadir}/gtk-doc/html/geonames/style.css
%{_datadir}/gtk-doc/html/geonames/geonames.devhelp2
