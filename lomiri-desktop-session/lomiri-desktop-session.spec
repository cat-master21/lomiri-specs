%global source_date_epoch_from_changelog 0

Name:       lomiri-desktop-session
Version:    0.1
Release:    1%{?dist}
Summary:    Configuration schemas for lomiri
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-desktop-session
Source0:    %{url}/-/archive/main/lomiri-desktop-session-main.tar.gz
BuildArch:  noarch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libsystemd)
BuildRequires: inotify-tools
BuildRequires: lomiri
BuildRequires: lomiri-system-compositor
BuildRequires: systemd-rpm-macros
Requires:      dbus-common
Requires:      inotify-tools
Requires:      lomiri

%description
Configuration schemas for lomiri.

%prep
%autosetup -n %{name}-main

%build
%cmake -DENABLE_TOUCH_SESSION=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/dm-lomiri-session
%{_bindir}/lomiri-*
%dir %{_prefix}/lib/lomiri-session
%{_prefix}/lib/lomiri-session/run-systemd-session
%{_userunitdir}/lomiri.service
%{_datadir}/lightdm/lightdm.conf.d/52-lomiri-touch.conf
%{_datadir}/lightdm/sessions/lomiri-touch.desktop
%dir %{_datadir}/lomiri-session
%{_datadir}/lomiri-session/lsc-wrapper
%{_datadir}/wayland-sessions/lomiri.desktop
