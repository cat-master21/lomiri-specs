%global source_date_epoch_from_changelog 0

Name:       lomiri-schemas
Version:    0.1.1
Release:    1%{?dist}
Summary:    Configuration schemas for lomiri
License:    LGPLv2+
URL:        https://gitlab.com/ubports/development/core/lomiri-schemas
Source0:    %{url}/-/archive/main/lomiri-schemas-main.tar.gz
BuildArch: noarch

BuildRequires: cmake
BuildRequires: gcc-c++

%description
Configuration schemas for lomiri.

%prep
%autosetup -n %{name}-main

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_datadir}/accountsservice/interfaces/*.xml
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pkgconfig/lomiri-schemas.pc
%{_datadir}/polkit-1/actions/com.lomiri.AccountsService.policy
%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/50-com.lomiri.AccountsService.pkla
