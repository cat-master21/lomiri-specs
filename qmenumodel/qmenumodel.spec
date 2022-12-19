%global source_date_epoch_from_changelog 0

Name:       qmenumodel
Version:    0.9.1
Release:    1%{?dist}
Summary:    Qt5 renderer for Ayatana Indicators
License:    LGPLv3
URL:        https://github.com/AyatanaIndicators/qmenumodel
Source0:    https://releases.ayatana-indicators.org/source/qmenumodel/qmenumodel-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)

%description
Qt bindings for GMenuModel that allows connecting to a menu model exposed on
D-Bus and presents it as a list model. It can be used to expose indicator or
application menus for applications using the Qt framework.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n qmenumodel-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING.LGPL
%{_libdir}/libqmenumodel.so.*
%dir %{_qt5_qmldir}/QMenuModel.1
%{_qt5_qmldir}/QMenuModel.1/libqmenumodel-qml.so
%{_qt5_qmldir}/QMenuModel.1/qmldir

%files devel
%license COPYING.LGPL
%dir %{_includedir}/qmenumodel
%{_includedir}/qmenumodel/*.h
%{_libdir}/libqmenumodel.so
%{_libdir}/pkgconfig/qmenumodel.pc
