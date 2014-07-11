%define modname	Pg
%define modver	2.1.1

Summary:	A libpq-based PostgreSQL interface for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	19
License:	GPLv2
Group:		Development/Perl
Url:		http://gborg.postgresql.org/project/pgperl/projdisplay.php
Source0:	%{modname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	postgresql-devel

%description
pgperl is an interface between Perl and PostgreSQL. This uses the
Perl5 API for C extensions to call the PostgreSQL libpq interface.
Unlike DBD:pg, pgperl tries to implement the libpq interface as
closely as possible.

You have a choice between two different interfaces:	the old
C-style interface and a new one, using a more Perl-ish style. The
old style has the benefit that existing libpq applications can
easily be ported to perl. The new style uses class packages and
might be more familiar to C++ programmers.

%prep
%setup -qn %{modname}-%{version}
# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
export POSTGRES_INCLUDE=`pg_config --includedir`
export POSTGRES_LIB=`pg_config --libdir`
%__perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
# make test needs a running PostgreSQL server
#%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*/*/Pg/Pg.so
%{perl_vendorlib}/*/*/Pg/autosplit.ix
%{perl_vendorlib}/*/Pg.pm
%{_mandir}/man3*/*

