%global source_date_epoch_from_changelog 0

Name:           click
Version:        0.5.0
Release:        1%{?dist}
Summary:        A small library for handling URLs over dbus

License:        LGPLv3+
URL:            https://gitlab.com/ubports/development/core/click
Source0:        %{url}/-/archive/%{version}/click-%{version}.tar.gz

BuildRequires: automake libtool
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: vala
BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: systemd-rpm-macros


%description
Click is a app building method.

%package devel
Summary:  Click development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and headers for Click.

%package -n python3-click
Summary:  Python3 files for Click
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-click
Python3 files for Click.

%package doc
Summary:   Documentation files for Click
BuildArch: noarch

%description doc
Provides HTML and Manpage (documentation) for Click.

%prep
%setup -q -n click-%{version}

%build
NOCONFIGURE=1 \
./autogen.sh

%configure
%make_build

%install
%make_install -- PYTHON_INSTALL_FLAGS="--root=%{buildroot}"

# Create documentation
pushd doc
make man
mv _build/man/click.1 %{buildroot}%{_mandir}/man1/click.1
make html
mkdir -p %{buildroot}%_pkgdocdir
mv _build/html %{buildroot}%_pkgdocdir
popd
mv README %{buildroot}%_pkgdocdir

# Debian / debhelper stuff not needed
rm -rf %{buildroot}%{_bindir}/dh_click %{buildroot}%{_datarootdir}/debhelper %{buildroot}%{_datarootdir}/perl5 %{buildroot}%{_mandir}/man1/dh_click.1
%files
%license LICENSE
%{_libdir}/libclick-0.4.so.*
%{_libdir}/click/libclickpreload.so


%files devel
%license LICENSE
%dir %{_includedir}/click-0.4
%{_includedir}/click-0.4/click.h
%{_libdir}/libclick-0.4.so
%{_libdir}/pkgconfig/click-0.4.pc
%{_libdir}/girepository-1.0/Click-0.4.typelib
%{_datarootdir}/gir-1.0/Click-0.4.gir

%files -n python3-click
%license LICENSE
%dir %{_sysconfdir}/click
%dir %{_sysconfdir}/click/databases
%{_sysconfdir}/click/databases/*.conf
%dir %{_sysconfdir}/schroot
%dir %{_sysconfdir}/schroot/click
%{_sysconfdir}/schroot/click/fstab
%{_bindir}/click
%{_unitdir}/click-system-hooks.service
%{_userunitdir}/click-user-hooks.service
%dir %{python3_sitelib}/click_package
%{python3_sitelib}/click_package/*.py
%dir %{python3_sitelib}/click_package/tests
%{python3_sitelib}/click_package/tests/*.py
%dir %{python3_sitelib}/click_package/tests/integration
%{python3_sitelib}/click_package/tests/integration/*.py
%dir %{python3_sitelib}/click_package/tests/integration/__pycache__
%{python3_sitelib}/click_package/tests/integration/__pycache__/*.pyc
%dir %{python3_sitelib}/click_package/tests/__pycache__
%{python3_sitelib}/click_package/tests/__pycache__/*.pyc
%dir %{python3_sitelib}/click_package/commands
%{python3_sitelib}/click_package/commands/*.py
%dir %{python3_sitelib}/click_package/commands/__pycache__
%{python3_sitelib}/click_package/commands/__pycache__/*.pyc
%dir %{python3_sitelib}/click_package/__pycache__
%{python3_sitelib}/click_package/__pycache__/*.pyc
%dir %{python3_sitelib}/click-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/click-%{version}-py%{python3_version}.egg-info/*.txt
%{python3_sitelib}/click-%{version}-py%{python3_version}.egg-info/PKG-INFO

%files doc
%license LICENSE
%{_mandir}/man1/click.1.gz
%dir %_pkgdocdir
%_pkgdocdir/README
%dir %_pkgdocdir/html
%_pkgdocdir/html/*.html
%_pkgdocdir/html/.buildinfo
%_pkgdocdir/html/*inv
%_pkgdocdir/html/*.js
%dir %_pkgdocdir/html/_sources
%_pkgdocdir/html/_sources/*.txt
%dir %_pkgdocdir/html/_static
%_pkgdocdir/html/_static/*.png
%_pkgdocdir/html/_static/*.css
%_pkgdocdir/html/_static/*.js
