Summary:	Python bingings for Gammu library
Summary(pl.UTF-8):	Wiązania języka Python dla biblioteki Gammu
Name:		python-gammu
Version:	0.21
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.cihar.com/python-gammu/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	3af56b5ac26d77b5eef00bfe4f2fb2df
URL:		http://icepick.info/
BuildRequires:	gammu-devel >= 1:1.11.91
BuildRequires:	pkgconfig >= 1:0.21-2
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	gammu-libs >= 1:1.11.91
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%dir %{py_sitedir}/gammu
%attr(755,root,root) %{py_sitedir}/gammu/*.so
%{py_sitedir}/gammu/*.py[co]
%{py_sitedir}/gammu/*.py
%{py_sitedir}/*.egg-info
%{_examplesdir}/%{name}-%{version}
