%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	gettext
Summary:	Locale-gettext perl module
Summary(pl):	Modu³ perla Locale-gettext
Name:		perl-Locale-gettext
Version:	1.01
Release:	2
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a perl5 module quickly written to gain access to the C library
functions for internatialization. They work just like the C versions.

%description -l pl
To jest modu³ perla umo¿liwiaj±cy dostêp do funkcji u³atwiaj±cych
umiêdzynarodowienie programów. Dzia³aj± tak samo jak ich wersje w C.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/Locale/*
%dir %{perl_sitearch}/auto/Locale/gettext
%{perl_sitearch}/auto/Locale/gettext/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Locale/gettext/*.so
%{_mandir}/man3/*
