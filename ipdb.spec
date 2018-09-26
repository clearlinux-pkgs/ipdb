#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipdb
Version  : 0.11
Release  : 1
URL      : https://files.pythonhosted.org/packages/80/fe/4564de08f174f3846364b3add8426d14cebee228f741c27e702b2877e85b/ipdb-0.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/fe/4564de08f174f3846364b3add8426d14cebee228f741c27e702b2877e85b/ipdb-0.11.tar.gz
Summary  : IPython-enabled pdb
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ipdb-bin
Requires: ipdb-python3
Requires: ipdb-license
Requires: ipdb-python
Requires: ipython
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : pexpect
BuildRequires : setuptools

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

%description python3
python3 components for the ipdb package.


%prep
%setup -q -n ipdb-0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537930878
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ipdb
cp COPYING.txt %{buildroot}/usr/share/doc/ipdb/COPYING.txt
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
/usr/share/doc/ipdb/COPYING.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
