#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colorama
Version  : 0.3.9
Release  : 53
URL      : https://pypi.debian.net/colorama/colorama-0.3.9.tar.gz
Source0  : https://pypi.debian.net/colorama/colorama-0.3.9.tar.gz
Summary  : Cross-platform colored terminal text.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: colorama-license = %{version}-%{release}
Requires: colorama-python = %{version}-%{release}
Requires: colorama-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/pypi/v/colorama.svg
:target: https://pypi.python.org/pypi/colorama/
:alt: Latest Version

%package legacypython
Summary: legacypython components for the colorama package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the colorama package.


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

%description python3
python3 components for the colorama package.


%prep
%setup -q -n colorama-0.3.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540417242
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1540417242
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/colorama
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/colorama/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/colorama/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
