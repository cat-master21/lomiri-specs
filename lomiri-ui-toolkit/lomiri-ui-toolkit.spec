%global source_date_epoch_from_changelog 0

Name:           lomiri-ui-toolkit
Version:        1.3.4
Release:        1%{?dist}
Summary:        QML components to ease the creation of beautiful applications in QML for Lomiri

License:        LGPLv3+
URL:            https://gitlab.com/ubports/development/core/lomiri-ui-toolkit
Source0:        %{url}/-/archive/main/lomiri-ui-toolkit-main.tar.gz

BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: qt5-rpm-macros
BuildRequires: qt5-qtdeclarative
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtgraphicaleffects
BuildRequires: qt5-qtfeedback
BuildRequires: qt5-mobility-devel
BuildRequires: qt5-pim-devel
BuildRequires: python3-rpm-macros
Requires:      qt5-qtgraphicaleffects
Requires:      qt5-qtfeedback


%description
This project consists of a set of QML components to ease the creation of
beautiful applications in QML for Lomiri.
QML alone lacks built-in components for basic widgets like Button, Slider,
Scrollbar, etc, meaning a developer has to build them from scratch. This
toolkit aims to stop this duplication of work, supplying beautiful components
ready-made and with a clear and consistent API.
These components are fully themeable so the look and feel can be easily
customized. Resolution independence technology is built in so UIs are scaled
to best suit the display.


%package devel
Summary:  Lomiri-ui-toolkit development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for lomiri-ui-toolkit.

%package -n python3-lomiriuitoolkit
Summary: Python3 files for Lomiri-ui-toolkit
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtdeclarative-devel

%description -n python3-lomiriuitoolkit
Python3 files for Lomiri-ui-toolkit.

%package doc
Summary: Documentation for Lomiri-ui-toolkit
BuildArch: noarch

%description doc
Documentation for Lomiri-ui-toolkit.

%package examples
Summary: Examples for Lomiri-ui-toolkit
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtdeclarative-devel


%description examples
Examples for Lomiri-ui-toolkit.

%prep
%autosetup -n lomiri-ui-toolkit-main

%build
%{qmake_qt5} 'CONFIG+=ubuntu-uitk-compat' 'CONFIG+=test'

%make_build

%install
%make_install INSTALL_ROOT=%{buildroot} STRIP=/bin/true
# Used by apicheck during tests only
rm -rf %{buildroot}%{_qt5_qmldir}/Extinct
%find_lang %{name}
%find_lang %{name}-gallery


%files -f %{name}.lang
%license COPYING
%{_libdir}/libLomiriGestures.so.*
%{_libdir}/libLomiriMetrics.so.*
%{_libdir}/libLomiriToolkit.so.*
%dir %{_qt5_plugindir}/lomiri
%dir %{_qt5_plugindir}/lomiri/metrics
%{_qt5_plugindir}/lomiri/metrics/*.so
%dir %{_qt5_qmldir}/Lomiri
%{_qt5_qmldir}/Lomiri/Components/
%{_qt5_qmldir}/Lomiri/Layouts/
%{_qt5_qmldir}/Lomiri/Metrics/
%{_qt5_qmldir}/Lomiri/PerformanceMetrics/
%{_qt5_qmldir}/Lomiri/Test/
%dir %{_qt5_qmldir}/Ubuntu
%{_qt5_qmldir}/Ubuntu/Components/
%{_qt5_qmldir}/Ubuntu/Layouts/
%{_qt5_qmldir}/Ubuntu/Metrics/
%{_qt5_qmldir}/Ubuntu/PerformanceMetrics/
%{_qt5_qmldir}/Ubuntu/Test/
%{_bindir}/lomiri-*


%files devel
%license COPYING
%{_libdir}/libLomiriGestures.so
%{_libdir}/libLomiriMetrics.so
%{_libdir}/libLomiriToolkit.so
%{_libdir}/*.prl
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/lomiri-ui-toolkit
%{_libdir}/lomiri-ui-toolkit/apicheck
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_qt5_includedir}/LomiriGestures/
%{_qt5_includedir}/LomiriMetrics/
%{_qt5_includedir}/LomiriToolkit/


%files -n python3-lomiriuitoolkit
%dir %{python3_sitelib}/lomiriuitoolkit
%{python3_sitelib}/lomiriuitoolkit/*.py
%{python3_sitelib}/lomiriuitoolkit/_custom_proxy_objects/
%{python3_sitelib}/lomiriuitoolkit/__pycache__/
%{python3_sitelib}/lomiriuitoolkit/tests/


%files doc
%license COPYING.CC-BY-SA-3.0
%{_qt5_docdir}/*.qch
%dir %{_datadir}/lomiri-ui-toolkit
%dir %{_datadir}/lomiri-ui-toolkit/doc
%{_datadir}/lomiri-ui-toolkit/doc/html/

%files examples -f %{name}-gallery.lang
%dir %{_qt5_examplesdir}/lomiri-ui-toolkit
%dir %{_qt5_examplesdir}/lomiri-ui-toolkit/examples
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/calculator/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/customtheme/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/jokes/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/locale/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/lomiri-ui-toolkit-gallery/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/unit-converter/
