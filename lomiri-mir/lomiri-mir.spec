%global source_date_epoch_from_changelog 0
# Force out of source build
%undefine __cmake_in_source_build

%ifnarch ppc64
# Enable LTO on non-ppc64 (c.f. rhbz#1515934)
%bcond_without lto
%endif

# Disable ctest run by default
# They take a long time and are generally broken in the build environment
%bcond_with run_tests

Name:           lomiri-mir
Version:        1.8.2
Release:        1%{?dist}
Summary:        Next generation display server (Lomiri version)

# mirclient is LGPLv2/LGPLv3, everything else is GPLv2/GPLv3
License:        (GPLv2 or GPLv3) and (LGPLv2 or LGPLv3)
URL:            https://mir-server.io/
Source0:        https://github.com/MirServer/mir/archive/refs/heads/release/1.8.tar.gz
Source1:        https://gitlab.com/ubports/development/core/packaging/mir/-/archive/ubports/focal/mir-ubports-focal.tar.gz
Patch0:         0007-temp-fix-for-removed-declaration-in-EGL-eglmesaext.h.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake, ninja-build, doxygen, graphviz, lcov, gcovr
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  boost-devel, protobuf-compiler, capnproto
BuildRequires:  python3-devel
BuildRequires:  glm-devel
BuildRequires:  protobuf-devel, protobuf-lite-devel, capnproto-devel
BuildRequires:  glog-devel, lttng-ust-devel, systemtap-sdt-devel
BuildRequires:  gflags-devel
BuildRequires:  python3-pillow

# Everything detected via pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm) >= 9.0.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmock) >= 1.8.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtest) >= 1.8.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml++-2.6)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(umockdev-1.0) >= 0.6
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(wlcs)

# pkgconfig(egl) is now from glvnd, so we need to manually pull this in for the Mesa specific bits...
BuildRequires:  mesa-libEGL-devel

# For some reason, this doesn't get pulled in automatically into the buildroot
BuildRequires:  libatomic

# For detecting the font for CMake
BuildRequires:  gnu-free-sans-fonts

# For validating the desktop file for mir-demos
BuildRequires:  %{_bindir}/desktop-file-validate

# Add architectures as verified to work
%ifarch %{ix86} x86_64 %{arm} aarch64
BuildRequires:  valgrind
%endif

%description
Mir is a display server running on linux systems,
with a focus on efficiency, robust operation,
and a well-defined driver model.

%package utils
Summary:       Utilities for Mir
Requires:      %{name}-server-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-client-libs%{?_isa} = %{version}-%{release}

%description utils
Utilities for Mir.

%package devel
Summary:       Development files for Mir
Requires:      %{name}-common-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-server-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-client-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-test-libs-static%{?_isa} = %{version}-%{release}

%description devel
This package provides the development files to create
applications that can run on Mir.

%package common-libs
Summary:       Common libraries for Mir
License:       LGPLv2 or LGPLv3

%description common-libs
This package provides the libraries common to be used
by Mir clients or Mir servers.

%package server-libs
Summary:       Server libraries for Mir
License:       GPLv2 or GPLv3
Requires:      %{name}-common-libs%{?_isa} = %{version}-%{release}

%description server-libs
This package provides the libraries for applications
that use the Mir server.

%package client-libs
Summary:       Client libraries for Mir
License:       LGPLv2 or LGPLv3
Requires:      dmz-cursor-themes
Requires:      %{name}-common-libs%{?_isa} = %{version}-%{release}
# debug extension for mirclient is gone...
Obsoletes:     %{name}-client-libs-debugext < 1.6.0

%description client-libs
This package provides the libraries for applications
that connect to a Mir server.

%package test-tools
Summary:       Testing tools for Mir
License:       GPLv2 or GPLv3
Requires:      %{name}-server-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-client-libs%{?_isa} = %{version}-%{release}
Recommends:    %{name}-demos
Recommends:    glmark2
Recommends:    xorg-x11-server-Xwayland
Requires:      wlcs

%description test-tools
This package provides tools for testing Mir.

%package demos
Summary:       Demonstration applications using Mir
License:       GPLv2 or GPLv3
Requires:      %{name}-server-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-client-libs%{?_isa} = %{version}-%{release}
Requires:      hicolor-icon-theme
Requires:      redhat-lsb-core
Recommends:    xorg-x11-server-Xwayland
Recommends:    xterm
# For some of the demos
Requires:      gnu-free-sans-fonts

%description demos
This package provides applications for demonstrating
the capabilities of the Mir display server.

%package doc
Summary:       Documentation for developing Mir based applications
BuildArch:     noarch

%description doc
This package provides documentation for developing Mir based
applications.

%package -n python3-lomiri-mir-perf-framework
Summary:       Performance benchmark framework for Mir
License:       GPLv2 or GPLv3
BuildArch:     noarch
%{?python_provide:%python_provide python3-lomiri-mir-perf-framework}

%description -n python3-lomiri-mir-perf-framework
This package provides a benchmark framework for Mir
and Mir based applications.

%package test-libs-static
Summary:       Testing framework library for Mir
License:       GPLv2 or GPLv3
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}

%description test-libs-static
This package provides the static library for building
Mir unit and integration tests.

%prep
%autosetup -p1 -n mir-release-1.8

# Apply Lomiri specific patches
tar -xf '%{SOURCE1}'
# Meant for phones
#rm -f mir-ubports-focal/debian/patches/ubports/0002-Nested-patchwork-Use-eglImage-for-software-buffers.patch
for i in mir-ubports-focal/debian/patches/ubports/*.patch; do patch -p1 < $i; done

# Backported https://github.com/MirServer/mir/commit/45a4ec0856512358a9002e4aff3fe07e79e0310c
sed -i 's/clear_color{0.0f, 0.0f, 0.0f, 0.0f}/clear_color{0.0f, 0.0f, 0.0f, 1.0f}/' src/renderers/gl/renderer.cpp

# Drop -Werror
sed -e "s/-Werror//g" -i CMakeLists.txt

# A bug with mesa-x11/wayland
# We always have gl in Fedora so it isn't really an issue
sed -i 's1BOOST_THROW_EXCEPTION(std::logic_error("DisplayBuffer does not support GL rendering"));1printf("DisplayBuffer does not support GL rendering");1' src/renderers/gl/renderer.cpp

%build

%cmake  -GNinja %{?with_lto:-DMIR_LINK_TIME_OPTIMIZATION=ON} \
        -DMIR_USE_PRECOMPILED_HEADERS=OFF \
        -DCMAKE_INSTALL_LIBEXECDIR="usr/libexec/mir" \
        -DMIR_EGL_SUPPORTED=ON \
        -DMIR_FATAL_COMPILE_WARNINGS=OFF \
        -DMIR_RUN_INTEGRATION_TESTS=OFF \
        -DMIR_BUILD_UNIT_TESTS=OFF \
        -DMIR_PLATFORM="mesa-x11;wayland;eglstream-kms"
        # mesa-kms is buggy and causes screen-tear
cmake --build redhat-linux-build -j$(nproc)

# Build documentation
%cmake_build --target doc

%install
%cmake_install

# Install documentation
pushd %{_vpath_builddir}
mkdir -p %{buildroot}%{_datadir}/doc/mir-doc
cp -a doc/html %{buildroot}%{_datadir}/doc/mir-doc
popd

# Nothing outside Mir should link to libmirprotobuf directly.
rm -fv %{buildroot}%{_libdir}/libmirprotobuf.so

%check
%if %{with run_tests}
# The tests are somewhat fiddly, so let's just run them but not block on them...
( %ctest ) || :
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/miral-shell.desktop


%files utils
%license COPYING.GPL*
%doc README.md
%{_bindir}/mirin
%{_bindir}/mirout
%{_bindir}/mirscreencast
%{_bindir}/mirvanity

%files devel
%license COPYING.*
%{_bindir}/mir_wayland_generator
%{_libdir}/libmir*.so
%{_libdir}/pkgconfig/mir*.pc
%{_includedir}/mir*

%files common-libs
%license COPYING.LGPL*
%doc README.md
%{_libdir}/libmircore.so.*
%{_libdir}/libmircommon.so.*
%{_libdir}/libmircookie.so.*
%{_libdir}/libmirplatform.so.*
%{_libdir}/libmirprotobuf.so.*
%dir %{_libdir}/mir

%files server-libs
%license COPYING.GPL*
%doc README.md
%{_libdir}/libmiral.so.*
%{_libdir}/libmirserver.so.*
%{_libdir}/libmirwayland.so.*
%dir %{_libdir}/mir/server-platform
#{_libdir}/mir/server-platform/graphics-mesa-kms.so.*
%{_libdir}/mir/server-platform/input-evdev.so.*
%{_libdir}/mir/server-platform/server-mesa-x11.so.*
%{_libdir}/mir/server-platform/graphics-eglstream-kms.so.*
%{_libdir}/mir/server-platform/graphics-wayland.so.*

%files client-libs
%license COPYING.LGPL*
%doc README.md
%{_libdir}/libmirclient.so.*
%dir %{_libdir}/mir/client-platform
%{_libdir}/mir/client-platform/mesa.so.*

%files test-tools
%license COPYING.GPL*
%{_bindir}/mir-*test*
%{_bindir}/mir_*test*
%{_bindir}/mir_stress
%dir %{_libdir}/mir/tools
%{_libdir}/mir/tools/libmirserverlttng.so
%{_libdir}/mir/tools/libmirclientlttng.so
%dir %{_libdir}/mir
%{_libdir}/mir/miral_wlcs_integration.so
%dir %{_libdir}/mir/server-platform
%{_libdir}/mir/server-platform/graphics-dummy.so
%{_libdir}/mir/server-platform/input-stub.so
%dir %{_libdir}/mir/client-platform
%{_libdir}/mir/client-platform/dummy.so

%files demos
%license COPYING.GPL*
%doc README.md
%{_bindir}/mir_demo_*
%{_bindir}/miral-*
%{_bindir}/mir-shell
%{_datadir}/applications/miral-shell.desktop
%{_datadir}/wayland-sessions/mir-shell.desktop
%{_datadir}/icons/hicolor/scalable/apps/ubuntu-logo.svg

%files doc
%license COPYING.*
%doc README.md
%{_datadir}/doc/mir-doc/html

%files -n python3-lomiri-mir-perf-framework
%license COPYING.GPL*
%doc README.md
%{python3_sitelib}/mir_perf_framework
%{python3_sitelib}/mir_perf_framework*.egg-info
%{_datadir}/mir-perf-framework

%files test-libs-static
%license COPYING.GPL*
%doc README.md
%{_libdir}/libmir-test-assist.a

%changelog
