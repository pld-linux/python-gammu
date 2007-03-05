Summary:	Python bingings for Gammu library
Summary(pl.UTF-8):	Wiązania języka Python dla biblioteki Gammu
Name:		python-gammu
Version:	0.19
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.cihar.com/python-gammu/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	ad967c35b6398545d4358d3f9915ef50
URL:		http://icepick.info/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	gammu-devel >= 1:1.10.0-0.1
BuildRequires:	pkgconfig >= 0.21-2
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gammu-libs >= 1:1.10.0-0.1

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
%attr(755,root,root) %{py_sitedir}/*.so
%{_examplesdir}/%{name}-%{version}/
