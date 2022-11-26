%global source_date_epoch_from_changelog 0

Name:           lomiri-app-launch
# Commit: 09ca48196381fbdeb32cf48b60a64a6cda77fd9f
# Update Release every now and then because there is no release
Version:        0.1.1
Release:        1%{?dist}
Summary:        Provides the Lomiri App Launch user space daemon

License:        GPLv3+
URL:            https://gitlab.com/ubports/development/core/lomiri-app-launch
Source0:        https://gitlab.com/cat-master21/lomiri-app-launch/-/archive/cat-master21-main-patch-82762/lomiri-app-launch-cat-master21-main-patch-82762.tar.gz
#Source0:        {url}/-/archive/main/lomiri-app-launch-main.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(zeitgeist-2.0)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: pkgconfig(mirserver)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(mirclient)
# Not in pkgconfig but required
BuildRequires: properties-cpp-devel
BuildRequires: libcurl-devel


%description
User space daemon for launching applications
Application launching system and associated utilities that is used to
launch applications in a standard and confined way.


%package devel
Summary:  Lomiri-app-launch development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for lomiri-app-launch.


%prep
%setup -q -n lomiri-app-launch-cat-master21-main-patch-82762

%build
for i in $(grep -r lib/@LOMIRI_APP_LAUNCH_ARCH@ --files-with-matches)
do
echo patching "$i"
sed -i 's?lib/@LOMIRI_APP_LAUNCH_ARCH@?lib64?' "$i"
done
sed -i 's/-Werror//' ./CMakeLists.txt
sed -i '/  -lpthread/a  -lgtest' ./liblomiri-app-launch/CMakeLists.txt
# For some reason the macro fails on both clang and gcc
cmake -DLOMIRI_APP_LAUNCH_ARCH=%{_arch} -DENABLE_COVERAGE=OFF -DENABLE_TESTS=OFF -B redhat-linux-build -DCMAKE_INSTALL_PREFIX:PATH=/usr

%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/liblomiri-app-launch.so.*
%{_bindir}/lomiri-app-*
%{_bindir}/lomiri-helper-*
%{_libexecdir}/lomiri-app-launch/


%files devel
%license COPYING
%{_libdir}/liblomiri-app-launch.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/girepository-1.0/LomiriAppLaunch-0.typelib
%{_datarootdir}/gir-1.0/LomiriAppLaunch-0.gir
%dir %{_includedir}/liblomiri-app-launch-0
%{_includedir}/liblomiri-app-launch-0/*.h
%dir %{_includedir}/liblomiri-app-launch-0/lomiri-app-launch
%{_includedir}/liblomiri-app-launch-0/lomiri-app-launch/*.h
