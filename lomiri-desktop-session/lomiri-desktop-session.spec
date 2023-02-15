%global source_date_epoch_from_changelog 0

Name:       lomiri-desktop-session
Version:    0.1
Release:    1%{?dist}
Summary:    Configuration schemas for lomiri
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-desktop-session
Source0:    %{url}/-/archive/main/lomiri-desktop-session-main.tar.gz
Patch0:     https://gitlab.com/cat-master21/lomiri-desktop-session/-/commit/72bac71a58877cf22d2f799bf5d855362dcbdb08.diff
Patch1:     https://gitlab.com/ubports/development/core/lomiri-desktop-session/-/commit/764dfe831cb13328f16b00214830096faca00bb6.diff
BuildArch:  noarch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libsystemd)
BuildRequires: inotify-tools
BuildRequires: lomiri
BuildRequires: lomiri-system-compositor
BuildRequires: systemd-rpm-macros
Recommends:    libayatana-common
Requires:      dbus-common
Requires:      inotify-tools
Requires:      lomiri

%description
Configuration schemas for lomiri.

%prep
%autosetup -n %{name}-main

%build
# https://gitlab.com/ubports/development/core/lomiri-desktop-session/-/issues/5
sed -i '/export MIR_SERVER_ENABLE_X11/d lomiri-session
sed -i '/export MIR_SERVER_X11_DISPLAYFD/d lomiri-session
#sed -i 's/export MIR_SERVER_ENABLE_X11/dbus-update-activation-environment --systemd MIR_SERVER_ENABLE_X11/' lomiri-session
#sed -i 's/export MIR_SERVER_X11_DISPLAYFD/dbus-update-activation-environment --systemd MIR_SERVER_X11_DISPLAYFD/' lomiri-session

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
