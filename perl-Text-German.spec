%define upstream_name    Text-German
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	German grundform reduction
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a rather incomplete implementaion of work done by Gudrun Putze-Meier. I
have to confess that I never read her original paper. So all credit belongs to
her, all bugs are mine. I tried to get some insight from an implementation of
two students of mine. They remain anonymous because their work was the wost
piece of code I ever saw. My code behaves mostly as their implementation did
except it is about 75 times faster.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Text
%{_mandir}/man3*/*

%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 405685
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-7mdv2009.0
+ Revision: 258616
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-6mdv2009.0
+ Revision: 246631
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.06-4mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-4mdv2008.0
+ Revision: 87005
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-3mdv2007.0
- better description and summary

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-2mdk
- Fix SPEC according to Perl Policy
    - URL

* Fri May 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-1mdk
- 0.06
- Make rpmbuildable

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.03-2mdk
- fix deps

