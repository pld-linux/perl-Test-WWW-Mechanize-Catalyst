#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	WWW-Mechanize-Catalyst
Summary:	Test::WWW::Mechanize::Catalyst - Test::WWW::Mechanize for Catalyst
#Summary(pl.UTF-8):	
Name:		perl-Test-WWW-Mechanize-Catalyst
Version:	0.45
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb6a345c2f101f417a5473cdd48a8d54
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Test-WWW-Mechanize-Catalyst/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::WWW::Mechanize) >= 1.14
BuildRequires:	perl-Catalyst >= 5.00
BuildRequires:	perl-Catalyst-Plugin-Session
BuildRequires:	perl-Catalyst-Plugin-Session-State-Cookie
BuildRequires:	perl-libwww >= 5.816
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-WWW-Mechanize >= 1.50
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Test::WWW::Mechanize::Catalyst module meshes the two to allow easy
testing of Catalyst applications without starting up a web server.

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
%doc CHANGES
%{perl_vendorlib}/Test/WWW/Mechanize/*.pm
%{_mandir}/man3/*
