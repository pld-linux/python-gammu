Summary:	Python bingings for Gammu library
Summary(pl.UTF-8):	Wiązania języka Python dla biblioteki Gammu
Name:		python-gammu
Version:	0.20
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.cihar.com/python-gammu/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	2cb7d6faae3d48588b6baac34ebb2fe4
URL:		http://icepick.info/
BuildRequires:	gammu-devel >= 1:1.10.0-0.1
BuildRequires:	pkgconfig >= 1:0.21-2
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	gammu-libs >= 1:1.10.0-0.1
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
%attr(755,root,root) %{py_sitedir}/gammu/*.so
%{py_sitedir}/gammu/*.py[co]
%{_examplesdir}/%{name}-%{version}
