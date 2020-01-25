#
# Conditional build:
%bcond_with	tests		# perform "make test"

%define	pdir	Test
%define	pnam	WWW-Mechanize-Catalyst
Summary:	Test::WWW::Mechanize::Catalyst - Test::WWW::Mechanize for Catalyst
Name:		perl-Test-WWW-Mechanize-Catalyst
Version:	0.56
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6057810d7f6f4517928d031cb85d1609
URL:		http://search.cpan.org/dist/Test-WWW-Mechanize-Catalyst/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::WWW::Mechanize) >= 1.14
BuildRequires:	perl-Catalyst >= 5.00
BuildRequires:	perl-Catalyst-Plugin-Session
BuildRequires:	perl-Catalyst-Plugin-Session-State-Cookie
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-WWW-Mechanize >= 1.50
BuildRequires:	perl-libwww >= 5.816
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Test::WWW::Mechanize::Catalyst module meshes the two to allow easy
testing of Catalyst applications without starting up a web server.

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
%doc CHANGES
%{perl_vendorlib}/Test/WWW/Mechanize/*.pm
%{_mandir}/man3/*
