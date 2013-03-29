%define upstream_name Pg
%define upstream_version 2.1.1

Summary:	A libpq-based PostgreSQL interface for Perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	13
License:	GPL
Group:		Development/Perl
Source0:	Pg-%{version}.tar.bz2
URL:		http://gborg.postgresql.org/project/pgperl/projdisplay.php
BuildRequires:	perl-devel
BuildRequires:	postgresql-devel
#BuildRequires:	postgresql-libs-devel

%description
pgperl is an interface between Perl and PostgreSQL. This uses the
Perl5 API for C extensions to call the PostgreSQL libpq interface.
Unlike DBD:pg, pgperl tries to implement the libpq interface as
closely as possible.

You have a choice between two different interfaces: the old
C-style interface and a new one, using a more Perl-ish style. The
old style has the benefit that existing libpq applications can
easily be ported to perl. The new style uses class packages and
might be more familiar to C++ programmers.

%prep
%setup -q -n Pg-%{version}
# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
export POSTGRES_INCLUDE=`pg_config --includedir`
export POSTGRES_LIB=`pg_config --libdir`
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
# make test needs a running PostgreSQL server
#%{__make} test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*/*/Pg/Pg.so
%{perl_vendorlib}/*/*/Pg/autosplit.ix
%{perl_vendorlib}/*/Pg.pm
%{_mandir}/man3*/*





%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-12mdv2012.0
+ Revision: 765594
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-11
+ Revision: 764122
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-10
+ Revision: 667292
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.1.1-9mdv2011.0
+ Revision: 564575
- rebuild for perl 5.12.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1.1-8mdv2010.1
+ Revision: 426568
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.1.1-7mdv2009.0
+ Revision: 223967
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.1.1-6mdv2008.1
+ Revision: 152233
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sat Feb 17 2007 Olivier Thauvin <nanardon@mandriva.org> 2.1.1-5mdv2007.0
+ Revision: 122058
- rebuild

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 2.1.1-4mdv2007.0
+ Revision: 53870
- rebuild && %%mkrel
- Import perl-Pg

* Tue May 02 2006 Stefan van der Eijk <stefan@eijk.nu> 2.1.1-3mdk
-_rebuild_for_sparc

* Wed May 11 2005 Buchan Milne <bgmilne@linux-mandrake.com> 2.1.1-2mdk
- Rebuild for postgresql-devel 8.0.2

* Tue Dec 07 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.1.1-1mdk
- New version 2.1.1.

