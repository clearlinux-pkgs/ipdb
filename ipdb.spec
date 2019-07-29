#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipdb
Version  : 0.12.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/87/a7/ef7d90574d641b61ce15a7cb578c7f72fef076deaa4c435aded3f3328519/ipdb-0.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/87/a7/ef7d90574d641b61ce15a7cb578c7f72fef076deaa4c435aded3f3328519/ipdb-0.12.1.tar.gz
Summary  : IPython-enabled pdb
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ipdb-bin = %{version}-%{release}
Requires: ipdb-license = %{version}-%{release}
Requires: ipdb-python = %{version}-%{release}
Requires: ipdb-python3 = %{version}-%{release}
Requires: ipython
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : setuptools

%description
IPython `pdb`
=============
.. image:: https://travis-ci.org/gotcha/ipdb.png?branch=master
:target: https://travis-ci.org/gotcha/ipdb
.. image:: https://codecov.io/gh/gotcha/ipdb/branch/master/graphs/badge.svg?style=flat
:target: https://codecov.io/gh/gotcha/ipdb?branch=master

%package bin
Summary: bin components for the ipdb package.
Group: Binaries
Requires: ipdb-license = %{version}-%{release}

%description bin
bin components for the ipdb package.


%package license
Summary: license components for the ipdb package.
Group: Default

%description license
license components for the ipdb package.


%package python
Summary: python components for the ipdb package.
Group: Default
Requires: ipdb-python3 = %{version}-%{release}

%description python
python components for the ipdb package.


%package python3
Summary: python3 components for the ipdb package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipdb package.


%prep
%setup -q -n ipdb-0.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564414419
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipdb
cp COPYING.txt %{buildroot}/usr/share/package-licenses/ipdb/COPYING.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipdb3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipdb/COPYING.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
