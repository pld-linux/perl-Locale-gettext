%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	gettext
Summary:	Locale::gettext Perl module
Summary(cs):	Modul Locale::gettext pro Perl
Summary(da):	Perlmodul Locale::gettext
Summary(de):	Locale::gettext Perl Modul
Summary(es):	Módulo de Perl Locale::gettext
Summary(fr):	Module Perl Locale::gettext
Summary(it):	Modulo di Perl Locale::gettext
Summary(ja):	Locale::gettext Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Locale::gettext ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Locale::gettext
Summary(pl):	Modu³ Perla Locale::gettext
Summary(pt):	Módulo de Perl Locale::gettext
Summary(pt_BR):	Módulo Perl Locale::gettext
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Locale::gettext
Summary(sv):	Locale::gettext Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Locale::gettext
Summary(zh_CN):	Locale::gettext Perl Ä£¿é
Name:		perl-Locale-gettext
Version:	1.01
Release:	3
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Obsoletes:	perl-gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::gettext is a perl5 module quickly written to gain access to
the C library functions for internatialization.  They work just like
the C versions.

%description -l pl
Locale::gettext jest modu³em perla umo¿liwiaj±cym dostêp do funkcji
u³atwiaj±cych umiêdzynarodowienie programów. Dzia³aj± one tak samo
jak ich wersje w C.

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
