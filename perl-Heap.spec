#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Heap
Version  : 0.80
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/J/JM/JMM/Heap-0.80.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JM/JMM/Heap-0.80.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0+
Requires: perl-Heap-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Heap routines...
This is a collection of routines for managing a heap data structure.

%package dev
Summary: dev components for the perl-Heap package.
Group: Development
Provides: perl-Heap-devel = %{version}-%{release}
Requires: perl-Heap = %{version}-%{release}

%description dev
dev components for the perl-Heap package.


%package perl
Summary: perl components for the perl-Heap package.
Group: Default
Requires: perl-Heap = %{version}-%{release}

%description perl
perl components for the perl-Heap package.


%prep
%setup -q -n Heap-0.80
cd %{_builddir}/Heap-0.80

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Heap.3
/usr/share/man/man3/Heap::Binary.3
/usr/share/man/man3/Heap::Binomial.3
/usr/share/man/man3/Heap::Elem.3
/usr/share/man/man3/Heap::Elem::Num.3
/usr/share/man/man3/Heap::Elem::NumRev.3
/usr/share/man/man3/Heap::Elem::Ref.3
/usr/share/man/man3/Heap::Elem::RefRev.3
/usr/share/man/man3/Heap::Elem::Str.3
/usr/share/man/man3/Heap::Elem::StrRev.3
/usr/share/man/man3/Heap::Fibonacci.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
