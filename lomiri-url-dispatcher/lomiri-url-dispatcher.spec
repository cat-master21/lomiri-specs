%global source_date_epoch_from_changelog 0

Name:           lomiri-url-dispatcher
# Commit: 09ca48196381fbdeb32cf48b60a64a6cda77fd9f
# Update Release
Version:        0.1.0
Release:        1
Summary:        A small library for handling URLs over dbus

License:        LGPLv3+
URL:            https://gitlab.com/ubports/development/core/lomiri-url-dispatcher
Source0:        %{url}/-/archive/main/lomiri-url-dispatcher-main.tar.gz

BuildRequires: systemd-rpm-macros
BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libapparmor)


%description
Lomiri-url-dispatcher is a small handler to take URLs and do what is appropriate with them.
That could be anything from launching a web browser to just starting an
application.  This is done over DBus because application confinement doesn't
allow for doing it from a confined application otherwise.  It's important
the that applications can't know about each other, so this is a fire and forget
type operation.


%package devel
Summary:  Lomiri-url-dispatcher development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for lomiri-url-dispatcher.


%prep
%setup -q -n lomiri-url-dispatcher-main
# Test libraries require a static gtest file
sed -i '/add_subdirectory(tests)/d' ./CMakeLists.txt

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/liblomiri-url-dispatcher.so.*
%{_bindir}/lomiri-url-*
%dir %{_libexecdir}/lomiri-app-launch/bad-url
%{_libexecdir}/lomiri-app-launch/bad-url/exec-tool
%dir %{_libexecdir}/lomiri-app-launch/url-overlay
%{_libexecdir}/lomiri-app-launch/url-overlay/exec-tool
%dir %{_libexecdir}/lomiri-url-dispatcher
%{_libexecdir}/lomiri-url-dispatcher/lomiri-*
%{_datadir}/applications/lomiri-url-dispatcher-gui.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%dir %{_datadir}/lomiri-url-dispatcher
%{_datadir}/lomiri-url-dispatcher/*.qml
%dir %{_datadir}/lomiri-url-dispatcher/gui
%{_datadir}/lomiri-url-dispatcher/gui/*.qml
%{_datadir}/lomiri-url-dispatcher/gui/*.svg
%{_userunitdir}/*.path
%{_userunitdir}/*.service


%files devel
%license COPYING
%{_libdir}/liblomiri-url-dispatcher.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/liblomiri-url-dispatcher
%{_includedir}/liblomiri-url-dispatcher/*.h
