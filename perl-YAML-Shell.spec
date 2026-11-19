#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	YAML
%define	pnam	Shell
Summary:	YAML::Shell - The YAML Test Shell
#Summary(pl.UTF-8):	
Name:		perl-YAML-Shell
Version:	0.71
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/YAML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e2c519385669f1e34ff6c57aab147fae
URL:		http://search.cpan.org/dist/YAML-Shell/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-YAML >= 0.67
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module supports the ysh command. It is not to be used in any
general way as a Perl module.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/YAML/*.pm
%{perl_vendorlib}/YAML/*.pod
%{_mandir}/man?/*
