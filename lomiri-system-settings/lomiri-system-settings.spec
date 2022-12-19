%global source_date_epoch_from_changelog 0

Name:       lomiri-system-settings
Version:    0.1
Release:    1%{?dist}
Summary:    The System Settings application for Lomiri
License:    GPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-system-settings
Source0:    %{url}/-/archive/main/lomiri-system-settings-main.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(geonames)
BuildRequires: pkgconfig(icu-i18n)
#BuildRequires: pkgconfig(libandroid-properties)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(QtGui)

%description
The system settings application (and library) for the Lomiri desktop enviroment.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n lomiri-system-settings-main
# Might be a fix, might not entirely work perhaps, needs testing
sed -i 's/act_user_get_formats_locale/act_user_get_real_name/' plugins/language/language-plugin.cpp
sed -i 's/act_user_set_formats_locale/act_user_set_real_name/' plugins/language/language-plugin.cpp

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_bindir}/lomiri-system-settings
%{_libdir}/libLomiriSystemSettings.so.*
%{_libdir}/libLomiriSystemSettingsPrivate.so.*
%dir %{_libdir}/lomiri-system-settings
%{_libdir}/lomiri-system-settings/*.so
%dir %{_libdir}/lomiri-system-settings/private
%dir %{_libdir}/lomiri-system-settings/private/Lomiri
%{_libdir}/lomiri-system-settings/private/Lomiri/SystemSettings/
%{_datadir}/applications/lomiri-system-settings.desktop
%{_datadir}/glib-2.0/schemas/com.lomiri.lomiri-system-settings.gschema.xml
%dir %{_datadir}/lomiri-system-settings
%{_datadir}/lomiri-system-settings/*.settings
%{_datadir}/lomiri-system-settings/*.svg
%{_datadir}/lomiri-system-settings/*.png
%{_datadir}/lomiri-system-settings/url-map.ini
%dir %{_datadir}/lomiri-system-settings/icons
%{_datadir}/lomiri-system-settings/icons/*.svg
%{_datadir}/lomiri-system-settings/qml-plugins/
%{_datadir}/lomiri-url-dispatcher/urls/lomiri-system-settings.url-dispatcher

%files devel
%license COPYING
%dir %{_includedir}/LomiriSystemSettings
%{_includedir}/LomiriSystemSettings/*.h
%{_includedir}/LomiriSystemSettings/ItemBase
%{_includedir}/LomiriSystemSettings/PluginInterface
%dir %{_includedir}/LomiriSystemSettings/private
%{_includedir}/LomiriSystemSettings/private/*.h
%{_libdir}/libLomiriSystemSettings.so
%{_libdir}/libLomiriSystemSettingsPrivate.so
%{_libdir}/pkgconfig/LomiriSystemSettings.pc
