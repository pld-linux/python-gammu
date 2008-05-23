Summary:	Python bingings for Gammu library
Summary(pl.UTF-8):	Wiązania języka Python dla biblioteki Gammu
Name:		python-gammu
Version:	0.26
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.cihar.com/python-gammu/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	886d0484b3eeaa306e61733d85407277
URL:		http://icepick.info/
BuildRequires:	gammu-devel >= 1:1.18.91
BuildRequires:	pkgconfig >= 1:0.21-2
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
%requires_eq	gammu-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bingings for Gammu library.

%description -l pl.UTF-8
Wiązania języka Python dla biblioteki Gammu.

%prep
%setup -q

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%dir %{py_sitedir}/gammu
%attr(755,root,root) %{py_sitedir}/gammu/*.so
%{py_sitedir}/gammu/*.py[co]
%{py_sitedir}/*.egg-info
%{_examplesdir}/%{name}-%{version}
