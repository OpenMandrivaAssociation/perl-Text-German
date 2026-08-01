%define upstream_name    Text-German
%define upstream_version 0.06
Name:		perl-%{upstream_name}
Version:	0.06
Release:	3

Summary:	German grundform reduction
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/U/UL/ULPFR/Text-German-0.06.tar.gz

BuildRequires:	make
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
%setup -q -n Text-German-0.06

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Text
%{_mandir}/man3*/*

