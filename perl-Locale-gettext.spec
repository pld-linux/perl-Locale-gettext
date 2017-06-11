%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	gettext
Summary:	Locale::gettext Perl module - message handling functions
Summary(pl.UTF-8):	Moduł Perla Locale::gettext - funkcje do obsługi komunikatów
Name:		perl-Locale-gettext
Version:	1.07
Release:	4
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pnam}-%{version}.tar.gz
# Source0-md5:	bc652758af65c24500f1d06a77415019
URL:		http://search.cpan.org/dist/gettext/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::gettext is a Perl 5 module quickly written to gain access to
the C library functions for internatialization.  They work just like
the C versions.

%description -l pl.UTF-8
Locale::gettext jest modułem Perla umożliwiającym dostęp do funkcji
ułatwiających umiędzynarodowienie programów. Działają one tak samo
jak ich wersje w C.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}" \
	LDDLFLAGS="%{rpmcflags} -shared"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Locale/gettext.pm
%dir %{perl_vendorarch}/auto/Locale/gettext
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/gettext/gettext.so
%{_mandir}/man3/Locale::gettext.3pm*
