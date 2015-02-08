%define upstream_name    Digest-GOST
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Uses the CryptoPro parameters from RFC 4357
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Digest/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(parent)
BuildRequires: perl-devel

%description
The 'Digest::GOST' module provides an interface to the GOST R 34.11-94
message digest algorithm.

This interface follows the conventions set forth by the 'Digest' module.

This module uses the default "test" parameters. To use the CryptoPro
parameters, use 'Digest::GOST::CryptoPro'.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

