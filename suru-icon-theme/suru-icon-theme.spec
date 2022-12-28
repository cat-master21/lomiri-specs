%global source_date_epoch_from_changelog 0

Name:       suru-icon-theme
Version:    20.05.1
Release:    1%{?dist}
Summary:    Suru icon theme for Lomiri desktop
License:    CC-BY-SA-3.0
URL:        https://gitlab.com/ubports/development/core/suru-icon-theme
Source0:    %{url}/-/archive/main/suru-icon-theme-main.tar.gz
BuildArch:  noarch

Requires:   hicolor-icon-theme

%description
Suru is a icon theme for Lomiri desktop.

%prep
%autosetup -n %{name}-main

%build
true

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -r suru %{buildroot}%{_datadir}/icons

%files
%license COPYING
%{_datadir}/icons/suru/
