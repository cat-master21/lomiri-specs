%global source_date_epoch_from_changelog 0

Name:       cmake-extras
Version:    1.0
Release:    1%{?dist}
Summary:    A collection of add-ons for the CMake build tool.
License:    GPLv3
URL:        https://github.com/ubports/cmake-extras
Source0:    https://github.com/ubports/cmake-extras/archive/f6b455df21fa483388a79db6366707310d68167e/cmake-extras.tar.gz
Source1:    https://gitlab.com/erlend.io/lomiri-on-fedora/-/raw/master/lomiri-cmake-extras/GMockConfig.cmake
Patch0:     https://gitlab.com/erlend.io/lomiri-on-fedora/-/raw/master/lomiri-cmake-extras/0001-add-hint-to-make-fedora-find-the-qmlplugindump.patch
BuildArch:  noarch

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
Requires:      gcovr
Requires:      gmock-devel
Requires:      lcov
Requires:      qt5-qtdeclarative-devel

%description
A collection of add-ons for the CMake build tool. Use to build lomiri. 

%global debug_package %{nil}

%prep
%autosetup -p1 -n cmake-extras-f6b455df21fa483388a79db6366707310d68167e
sed 's/#!\/bin\/sh/#!\/usr\/bin\/sh/' src/FormatCode/formatcode.in > src/FormatCode/formatcode.in
sed 's/#!\/bin\/sh/#!\/usr\/bin\/sh/' src/CopyrightTest/check_copyright.sh > src/CopyrightTest/check_copyright.sh
sed 's/python/python3/' src/IncludeChecker/include_checker.py > src/IncludeChecker/include_checker.py

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make

%install
cd build
make DESTDIR=%{buildroot} install
cp %{SOURCE1} %{buildroot}/usr/share/cmake/GMock/

%files
/usr/share/cmake/CopyrightTest/CopyrightTestConfig.cmake
/usr/share/cmake/CopyrightTest/check_copyright.sh
/usr/share/cmake/CoverageReport/CoverageReportConfig.cmake
/usr/share/cmake/CoverageReport/EnableCoverageReport.cmake
/usr/share/cmake/DoxygenBuilder/Doxyfile.in
/usr/share/cmake/DoxygenBuilder/DoxygenBuilderConfig.cmake
/usr/share/cmake/GDbus/GDbusConfig.cmake
/usr/share/cmake/GMock/GMockConfig.cmake
/usr/share/cmake/GSettings/GSettingsConfig.cmake
/usr/share/cmake/Intltool/IntltoolConfig.cmake
/usr/share/cmake/Lcov/LcovConfig.cmake
/usr/share/cmake/QmlPlugins/QmlPluginsConfig.cmake
/usr/share/cmake/FormatCode/unity-api.clang-format
/usr/share/cmake/FormatCode/formatcode.in
/usr/share/cmake/FormatCode/formatcode_format.cmake.in
/usr/share/cmake/FormatCode/unity-api.astyle
/usr/share/cmake/FormatCode/formatcode_test.cmake.in
/usr/share/cmake/FormatCode/FormatCodeConfig.cmake
/usr/share/cmake/FormatCode/formatcode_common.cmake
/usr/share/cmake/gcovr/gcovrConfig.cmake
/usr/share/cmake/IncludeChecker/IncludeCheckerConfig.cmake
/usr/share/cmake/IncludeChecker/deps
/usr/share/cmake/IncludeChecker/include_checker.py
