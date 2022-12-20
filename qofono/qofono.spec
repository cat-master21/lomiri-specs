%global source_date_epoch_from_changelog 0

Name:       qofono
Summary:    A library of Qt 5 bindings for ofono
Version:    0.115
Release:    1%{?dist}
License:    LGPLv2
URL:        https://github.com/sailfishos/libqofono
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz
Source1:    https://gitlab.com/ubports/development/core/packaging/libqofono/-/archive/ubports/latest/libqofono-ubports-latest.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Test)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This package contains Qt bindings for ofono cellular service
interfaces.

%package devel
Summary:    Development files for ofono Qt bindings
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development header files for the ofono Qt bindings.

%package tests
Summary:    Qml tests and examples for the ofono Qt bindings
Requires:   %{name} = %{version}-%{release}
#Requires:   blts-tools
#Requires:   phonesim
#Requires:   mce-tools

%description tests
This package contains qml tests and examples for ofono Qt bindings.

%prep
%setup -q -n libqofono-%{version}
# Apply Lomiri specific patches
tar -xf '%{SOURCE1}'
sed -i 'sX$(dpkg-architecture -qDEB_HOST_MULTIARCH)/XX' libqofono-ubports-latest/debian/patches/2001_path-adjustments.patch
for i in $(cat libqofono-ubports-latest/debian/patches/series); do patch --no-backup-if-mismatch -f -p1 --fuzz=0 < libqofono-ubports-latest/debian/patches/$i; done

%build
export QT_SELECT=5
%qmake_qt5 "VERSION=$(sed 's/+.*//' <<<"%{version}")"
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libqofono-qt5.so.*
%dir %{_qt5_qmldir}/MeeGo
%{_qt5_qmldir}/MeeGo/QOfono/

%files devel
%license COPYING
%{_libdir}/libqofono-qt5.prl
%{_libdir}/libqofono-qt5.so
%{_libdir}/pkgconfig/qofono-qt5.pc
%dir %{_includedir}/qofono-qt5
%{_includedir}/qofono-qt5/*.h
%dir %{_includedir}/qofono-qt5/dbus
%{_includedir}/qofono-qt5/dbus/ofono*.xml
%{_qt5_datadir}/mkspecs/features/qofono-qt5.prf

%files tests
%license COPYING
%dir %{_libexecdir}/libqofono-qt5
%{_libexecdir}/libqofono-qt5/tests/
%{_libexecdir}/libqofono-qt5/ofonotest
%dir %{_datadir}/libqofono-qt5
%dir %{_datadir}/libqofono-qt5/qml
%dir %{_datadir}/libqofono-qt5/qml/ofonotest
%{_datadir}/libqofono-qt5/qml/ofonotest/main.qml
