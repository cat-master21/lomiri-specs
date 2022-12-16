%global source_date_epoch_from_changelog 0

Name:       gsettings-qt
Version:    1.0
Release:    1%{?dist}
Summary:    QML Bindings for GSettings
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/gsettings-qt
Source0:    %{url}/-/archive/main/gsettings-qt-main.tar.gz

BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative
BuildRequires: qt5-qtdeclarative-devel

Requires: %{name}%{?_isa} = %{version}-%{release}
%description
QML Bindings for GSettings
Expose QML bindings for GSettings
Library to access GSettings from Qt
Library to access GSettings from Qt

%package devel
Summary: Development files for %{name}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n gsettings-qt-main

%build
%qmake_qt5
sed -i 's/<QGSettings>/"qgsettings.h"/' tests/cpptest.cpp
QT_QPA_PLATFORM=minimal LD_LIBRARY_PATH=../src GSETTINGS_BACKEND=memory GSETTINGS_SCHEMA_DIR=. %make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
# Files under are part of coreutils and cpptest packages
rm -rf %{buildroot}/usr/tests

%files
%license COPYING
%{_libdir}/libgsettings-qt.so.1
%{_libdir}/libgsettings-qt.so.1.0
%{_libdir}/libgsettings-qt.so.1.0.0
%{_libdir}/qt5/qml/GSettings.1.0/libGSettingsQmlPlugin.so
%{_libdir}/qt5/qml/GSettings.1.0/plugins.qmltypes
%{_libdir}/qt5/qml/GSettings.1.0/qmldir

%files devel
%license COPYING
%{_includedir}/qt5/QGSettings/QGSettings
%{_includedir}/qt5/QGSettings/qgsettings.h
%{_libdir}/libgsettings-qt.so
%{_libdir}/pkgconfig/gsettings-qt.pc
