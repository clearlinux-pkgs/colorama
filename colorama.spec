#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colorama
Version  : 0.3.3
Release  : 10
URL      : https://pypi.python.org/packages/source/c/colorama/colorama-0.3.3.tar.gz
Source0  : https://pypi.python.org/packages/source/c/colorama/colorama-0.3.3.tar.gz
Summary  : Cross-platform colored terminal text.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: colorama-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://travis-ci.org/tartley/colorama.svg?branch=double-indent
:target: https://travis-ci.org/tartley/colorama

%package python
Summary: python components for the colorama package.
Group: Default

%description python
python components for the colorama package.


%prep
%setup -q -n colorama-0.3.3

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
