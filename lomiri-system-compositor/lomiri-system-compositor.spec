%global source_date_epoch_from_changelog 0

Name:       lomiri-system-compositor
Version:    1.0.0
Release:    2%{?dist}
Summary:    Mir system compositor for Lomiri
License:    GPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-system-compositor
Source0:    %{url}/-/archive/main/lomiri-system-compositor-main.tar.gz

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: deviceinfo-devel
BuildRequires: lomiri-mir-devel
BuildRequires: python3-pillow-devel
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(deviceinfo)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(dbus-1)

%description
Mir System Compositor
This is the system compositor using the Mir display server.  If the Lomiri
System Compositor can't start, LightDM will fallback to plain Xorg display
server.

%prep
%autosetup -n %{name}-main

%build
sed -i '20 i#include <stdexcept>' spinner/eglapp.cpp
sed -i '23 i#include <stdexcept>' spinner/miregl.cpp
%cmake -DCMAKE_INSTALL_SYSCONFDIR=/etc
%cmake_build

%install
# manpages are in debian/ could be added later
%cmake_install
# Not really useful and some already done
rm -rf %{buildroot}%{_bindir}/lsc*

%files
%{_sysconfdir}/dbus-1/system.d/com.lomiri.SystemCompositor.conf
%{_bindir}/lomiri-system-compositor-spinner
%{_sbindir}/lomiri-system-compositor
%{_datadir}/dbus-1/interfaces/*.xml
