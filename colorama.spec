#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colorama
Version  : 0.3.7
Release  : 38
URL      : https://pypi.debian.net/colorama/colorama-0.3.7.tar.gz
Source0  : https://pypi.debian.net/colorama/colorama-0.3.7.tar.gz
Summary  : Cross-platform colored terminal text.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: colorama-python3
Requires: colorama-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://pypip.in/version/colorama/badge.svg
:target: https://pypi.python.org/pypi/colorama/
:alt: Latest Version

%package legacypython
Summary: legacypython components for the colorama package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the colorama package.


%package python
Summary: python components for the colorama package.
Group: Default
Requires: colorama-python3

%description python
python components for the colorama package.


%package python3
Summary: python3 components for the colorama package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colorama package.


%prep
%setup -q -n colorama-0.3.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519398492
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1519398492
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
