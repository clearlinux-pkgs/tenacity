#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tenacity
Version  : 5.1.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/e3/8c/0be748642bbc63774df0705fda4ce42cea37edbd62b7ff351d74b4dc34fb/tenacity-5.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e3/8c/0be748642bbc63774df0705fda4ce42cea37edbd62b7ff351d74b4dc34fb/tenacity-5.1.0.tar.gz
Summary  : Retry code until it succeeeds
Group    : Development/Tools
License  : Apache-2.0
Requires: tenacity-license = %{version}-%{release}
Requires: tenacity-python = %{version}-%{release}
Requires: tenacity-python3 = %{version}-%{release}
Requires: monotonic
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : monotonic
BuildRequires : setuptools_scm
BuildRequires : six

%description
Tenacity
========
.. image:: https://img.shields.io/pypi/v/tenacity.svg
:target: https://pypi.python.org/pypi/tenacity

%package license
Summary: license components for the tenacity package.
Group: Default

%description license
license components for the tenacity package.


%package python
Summary: python components for the tenacity package.
Group: Default
Requires: tenacity-python3 = %{version}-%{release}

%description python
python components for the tenacity package.


%package python3
Summary: python3 components for the tenacity package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tenacity package.


%prep
%setup -q -n tenacity-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565944125
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tenacity
cp LICENSE %{buildroot}/usr/share/package-licenses/tenacity/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tenacity/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
