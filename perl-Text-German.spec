%define upstream_name    Text-German
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    German grundform reduction
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Text
%{_mandir}/man3*/*
