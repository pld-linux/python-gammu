%define		module	python-gammu
Summary:	Python bindings for Gammu library.
Name:		%{module}
Version:	2.3
Release:	4
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://dl.cihar.com/python-gammu/%{module}-%{version}.tar.bz2
# Source0-md5:	e92b13cb6fa9681c48981340ffadd251
URL:		http://http://wammu.eu/python-gammu/
BuildRequires:	gammu-devel >= 1.34.0
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	glibc >= 2.4
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Gammu library.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

install examples/data/*.* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/data
install examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
#install examples/data/*.* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/data

sed -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python}\1,' \
      $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/gammu
%attr(755,root,root) %{py_sitedir}/gammu/*.so
%{py_sitedir}/gammu/*.py[co]
%{py_sitedir}/python_gammu-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
