#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kgamma5
Version  : 5.27.3
Release  : 80
URL      : https://download.kde.org/stable/plasma/5.27.3/kgamma5-5.27.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.3/kgamma5-5.27.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.3/kgamma5-5.27.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: kgamma5-data = %{version}-%{release}
Requires: kgamma5-lib = %{version}-%{release}
Requires: kgamma5-license = %{version}-%{release}
Requires: kgamma5-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the kgamma5 package.
Group: Data

%description data
data components for the kgamma5 package.


%package doc
Summary: doc components for the kgamma5 package.
Group: Documentation

%description doc
doc components for the kgamma5 package.


%package lib
Summary: lib components for the kgamma5 package.
Group: Libraries
Requires: kgamma5-data = %{version}-%{release}
Requires: kgamma5-license = %{version}-%{release}

%description lib
lib components for the kgamma5 package.


%package license
Summary: license components for the kgamma5 package.
Group: Default

%description license
license components for the kgamma5 package.


%package locales
Summary: locales components for the kgamma5 package.
Group: Default

%description locales
locales components for the kgamma5 package.


%prep
%setup -q -n kgamma5-5.27.3
cd %{_builddir}/kgamma5-5.27.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679523566
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1679523566
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kgamma5
cp %{_builddir}/kgamma5-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kgamma5/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kgamma5-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kgamma5/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
pushd clr-build
%make_install
popd
%find_lang kcmkgamma

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kgamma/pics/background.png
/usr/share/kgamma/pics/cmyscale.png
/usr/share/kgamma/pics/darkgrey.png
/usr/share/kgamma/pics/greyscale.png
/usr/share/kgamma/pics/lightgrey.png
/usr/share/kgamma/pics/midgrey.png
/usr/share/kgamma/pics/rgbscale.png

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/cs/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/cs/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/de/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/en/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/es/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/et/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/et/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/fr/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/id/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/id/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/it/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/nl/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/pt/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/ru/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/sv/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/kgamma5/index.docbook
/usr/share/doc/HTML/uk/kcontrol/kgamma5/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/kgamma5/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/plasma/kcminit/kcm_kgamma_init.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings/kcm_kgamma.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kgamma5/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kgamma5/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kcmkgamma.lang
%defattr(-,root,root,-)

