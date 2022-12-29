%global source_date_epoch_from_changelog 0

Name:    lomiri-keyboard
Summary: Ubuntu Touch keyboard as a maliit plugin
Version: 5.15
Release: 1%{?dist}

License: LGPLv3 AND BSD-3-Clause
URL:     https://gitlab.com/ubports/development/core/lomiri-keyboard
Source0: %{url}/-/archive/main/lomiri-keyboard-main.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pkgconfig(QtCore)
BuildRequires: qt5-doctools
BuildRequires: systemd-rpm-macros
BuildRequires: qt5-rpm-macros
BuildRequires: libpinyin-devel
BuildRequires: hunspell-devel
BuildRequires: maliit-framework-devel
Recommends:    lomiri
Requires:      maliit-framework

%description
Lomiri keyboard is a QML and C++ based Keyboard Plugin for Maliit, 
based on the Maliit Reference plugin, taking into account the special UI/UX requests of Ubuntu Touch.

%package devel
Summary: Lomiri Keyboard development files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -n lomiri-keyboard-main

%build
# Relies on presage
rm ./plugins/plugins.pro
sed -i '/plugins \\/d' lomiri-keyboard.pro

mkdir redhat-linux-build
cp -r po redhat-linux-build
cd ./redhat-linux-build
# CONFIG+=enable-presage but presage is not available
%qmake_qt5 MALIIT_DEFAULT_PROFILE=lomiri CONFIG+=release CONFIG+=doc CONFIG+=notests CONFIG+=enable-hunspell CONFIG+=enable-pinyin ..

%make_build

%install
cd ./redhat-linux-build
%make_install INSTALL_ROOT=%{buildroot}
cd ../
%find_lang %{name}
mkdir -p %{buildroot}%{_userunitdir}
cp debian/systemd/maliit-server.service %{buildroot}%{_userunitdir}

%files -f %{name}.lang
%license COPYING COPYING.BSD
%{_userunitdir}/maliit-server.service
%{_libdir}/maliit/plugins/liblomiri-keyboard-plugin.so
%dir %{_qt5_qmldir}/Lomiri/Keyboard
%{_qt5_qmldir}/Lomiri/Keyboard/liblomiri-keyboard-qml.so
%{_qt5_qmldir}/Lomiri/Keyboard/qmldir
%{_datadir}/glib-2.0/schemas/com.lomiri.keyboard.maliit.gschema.xml
%{_datadir}/maliit/plugins/lomiri-keyboard/

%files devel
%license COPYING COPYING.BSD
%dir %{_includedir}/lomiri-keyboard
%{_includedir}/lomiri-keyboard/languageplugininterface.h

%changelog
