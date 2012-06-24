%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	gettext
Summary:	Locale::gettext Perl module
Summary(cs):	Modul Locale::gettext pro Perl
Summary(da):	Perlmodul Locale::gettext
Summary(de):	Locale::gettext Perl Modul
Summary(es):	M�dulo de Perl Locale::gettext
Summary(fr):	Module Perl Locale::gettext
Summary(it):	Modulo di Perl Locale::gettext
Summary(ja):	Locale::gettext Perl �⥸�塼��
Summary(ko):	Locale::gettext �� ����
Summary(nb):	Perlmodul Locale::gettext
Summary(pl):	Modu� Perla Locale::gettext
Summary(pt):	M�dulo de Perl Locale::gettext
Summary(pt_BR):	M�dulo Perl Locale::gettext
Summary(ru):	������ ��� Perl Locale::gettext
Summary(sv):	Locale::gettext Perlmodul
Summary(uk):	������ ��� Perl Locale::gettext
Summary(zh_CN):	Locale::gettext Perl ģ��
Name:		perl-Locale-gettext
Version:	1.01
Release:	8
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	dce77a8733a0e88d8c5fb5bd86ec5f0a
Patch0:		%{name}-include.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::gettext is a perl5 module quickly written to gain access to
the C library functions for internatialization.  They work just like
the C versions.

%description -l pl
Locale::gettext jest modu�em perla umo�liwiaj�cym dost�p do funkcji
u�atwiaj�cych umi�dzynarodowienie program�w. Dzia�aj� one tak samo
jak ich wersje w C.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Locale/*
%dir %{perl_vendorarch}/auto/Locale/gettext
%{perl_vendorarch}/auto/Locale/gettext/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/gettext/*.so
%{_mandir}/man3/*
