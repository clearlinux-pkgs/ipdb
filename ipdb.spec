#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipdb
Version  : 0.13.6
Release  : 26
URL      : https://files.pythonhosted.org/packages/fd/74/ebed6f1bda0dbd7641e19809882e060fb9e3fd1ff0e44c3071ec06c08078/ipdb-0.13.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/fd/74/ebed6f1bda0dbd7641e19809882e060fb9e3fd1ff0e44c3071ec06c08078/ipdb-0.13.6.tar.gz
Summary  : IPython-enabled pdb
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ipdb-bin = %{version}-%{release}
Requires: ipdb-license = %{version}-%{release}
Requires: ipdb-python = %{version}-%{release}
Requires: ipdb-python3 = %{version}-%{release}
Requires: ipython
Requires: setuptools
Requires: toml
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : setuptools
BuildRequires : toml

%description
=============

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
Provides: pypi(ipdb)
Requires: pypi(ipython)
Requires: pypi(setuptools)
Requires: pypi(toml)

%description python3
python3 components for the ipdb package.


%prep
%setup -q -n ipdb-0.13.6
cd %{_builddir}/ipdb-0.13.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615230923
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipdb
cp %{_builddir}/ipdb-0.13.6/COPYING.txt %{buildroot}/usr/share/package-licenses/ipdb/eac15b69f9f0a12e02459ba5c6be4fa52c10f364
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
/usr/share/package-licenses/ipdb/eac15b69f9f0a12e02459ba5c6be4fa52c10f364

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
