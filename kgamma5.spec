#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kgamma5
Version  : 5.14.1
Release  : 4
URL      : https://download.kde.org/stable/plasma/5.14.1/kgamma5-5.14.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.14.1/kgamma5-5.14.1.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.14.1/kgamma5-5.14.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kgamma5-data = %{version}-%{release}
Requires: kgamma5-lib = %{version}-%{release}
Requires: kgamma5-license = %{version}-%{release}
Requires: kgamma5-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kgamma5-5.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539702114
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539702114
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kgamma5
cp COPYING %{buildroot}/usr/share/package-licenses/kgamma5/COPYING
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
/usr/share/kservices5/kgamma.desktop

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
/usr/lib64/qt5/plugins/kcm_kgamma.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kgamma5/COPYING

%files locales -f kcmkgamma.lang
%defattr(-,root,root,-)

