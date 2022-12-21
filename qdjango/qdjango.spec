%global source_date_epoch_from_changelog 0

Name:       qdjango
Version:    0.6.2
Release:    1%{?dist}
Summary:    A web framework written in C++ and built on top of the Qt library
License:    LGPLv2
URL:        https://github.com/jlaine/qdjango
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:    https://salsa.debian.org/debian/qdjango/-/archive/debian/%{version}-3.3/qdjango-debian-%{version}-3.3.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: doxygen

%description
QDjango is a web framework written in C++ and built on top of the Qt library.
Where possible, it tries to follow django's API, hence its name.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documenation for %{name}
BuildArch: noarch

%description doc
The %{name}-doc contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}
# Apply fixes from debian/lomiri
tar -xf '%{SOURCE1}'
for i in $(cat qdjango-debian-%{version}-3.3/debian/patches/series); do patch --no-backup-if-mismatch -f -p1 --fuzz=0 < qdjango-debian-%{version}-3.3/debian/patches/$i; done

%build
%qmake_qt5 PREFIX=%{_exec_prefix} LIBDIR=%{_lib}
%make_build
%make_build docs

%install
%make_install INSTALL_ROOT=%{buildroot}
# Aren't needed and already ran plus contain rpaths in every single file underneath
rm -rf %{buildroot}%{_prefix}/tests

%files
%license LICENSE.LGPL
%{_libdir}/libqdjango-db.so.*
%{_libdir}/libqdjango-http.so.*

%files devel
%license LICENSE.LGPL
%dir %{_includedir}/qdjango
%dir %{_includedir}/qdjango/db
%{_includedir}/qdjango/db/*.h
%dir %{_includedir}/qdjango/http
%{_includedir}/qdjango/http/*.h
%{_libdir}/libqdjango-db.so
%{_libdir}/libqdjango-http.so
%{_libdir}/pkgconfig/qdjango-db.pc
%{_libdir}/pkgconfig/qdjango-http.pc

%files doc
%dir %{_docdir}/qdjango
%{_docdir}/qdjango/html/
