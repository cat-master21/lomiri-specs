%global source_date_epoch_from_changelog 0

Name:           dbus-test-runner
Version:        19.04.0
Release:        1
Summary:        A small utility to run executables under a new DBus session for testing
License:        GPLv3+
URL:            https://launchpad.net/dbus-test-runner
Source0:        %{url}/19.04/%{version}/+download/dbus-test-runner-%{version}.tar.gz

BuildRequires: automake libtool mate-common
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(dbus-glib-1)


%description
A small little utility to run a couple of executables under a new DBus session for testing.

%package devel
Summary:  dbus-test-runner development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and headers for dbus-test-runner.


%prep
%setup -q -n dbus-test-runner-%{version}

%build
NOCONFIGURE=1 autoreconf -fi

%configure
%make_build

%install
%make_install
# Don't package static files
rm -rf %{buildroot}%{_libdir}/libdbustest.a


%files
%license COPYING
%{_libdir}/libdbustest.so.*
%dir %{_libexecdir}/dbus-test-runner
%{_libexecdir}/dbus-test-runner/dbus-test-watchdog
%{_bindir}/dbus-test-runner
%dir %{_datarootdir}/dbus-test-runner
%{_datarootdir}/dbus-test-runner/*.conf
%{_datarootdir}/dbus-test-runner/dbus-test-bustle-handler


%files devel
%license COPYING
%dir %{_includedir}/libdbustest-1
%dir %{_includedir}/libdbustest-1/libdbustest
%{_includedir}/libdbustest-1/libdbustest/*.h
%{_libdir}/libdbustest.so
%{_libdir}/pkgconfig/dbustest-1.pc
