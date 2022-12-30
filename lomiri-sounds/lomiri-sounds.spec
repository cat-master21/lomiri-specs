%global source_date_epoch_from_changelog 0

Name:       lomiri-sounds
Summary:    Ring-tones and notification tones included with Ubuntu Touch
Version:    22.02
Release:    1%{?dist}
License:    CC-BY-SA-3.0
URL:        https://gitlab.com/ubports/development/core/lomiri-sounds
Source0:    %{url}/-/archive/main/lomiri-sounds-main.tar.gz

BuildRequires:  cmake

%description
Lomiri sounds contains the ringtones and notification tones recommended for the Lomiri stack.

%prep
%autosetup -n %{name}-main

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_libdir}

%files
%{_libdir}/pkgconfig/lomiri-sounds.pc
%dir %{_datadir}/sounds/lomiri
%{_datadir}/sounds/lomiri/camera/
%{_datadir}/sounds/lomiri/notifications/
%{_datadir}/sounds/lomiri/ringtones/
