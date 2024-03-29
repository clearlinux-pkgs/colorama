#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colorama
Version  : 0.4.4
Release  : 81
URL      : https://files.pythonhosted.org/packages/1f/bb/5d3246097ab77fa083a61bd8d3d527b7ae063c7d8e8671b1cf8c4ec10cbe/colorama-0.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/bb/5d3246097ab77fa083a61bd8d3d527b7ae063c7d8e8671b1cf8c4ec10cbe/colorama-0.4.4.tar.gz
Summary  : Cross-platform colored terminal text.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: colorama-license = %{version}-%{release}
Requires: colorama-python = %{version}-%{release}
Requires: colorama-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/pypi/v/colorama.svg
:target: https://pypi.org/project/colorama/
:alt: Latest Version

%package license
Summary: license components for the colorama package.
Group: Default

%description license
license components for the colorama package.


%package python
Summary: python components for the colorama package.
Group: Default
Requires: colorama-python3 = %{version}-%{release}

%description python
python components for the colorama package.


%package python3
Summary: python3 components for the colorama package.
Group: Default
Requires: python3-core
Provides: pypi(colorama)

%description python3
python3 components for the colorama package.


%prep
%setup -q -n colorama-0.4.4
cd %{_builddir}/colorama-0.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635713627
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/colorama
cp %{_builddir}/colorama-0.4.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/colorama/151478b5f4a6291addb13da92ef3534597ed39a4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/colorama/151478b5f4a6291addb13da92ef3534597ed39a4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
