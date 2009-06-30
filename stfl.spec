%define name	stfl
%define version 0.21
%define release %mkrel 1
%define major	0

%define libname   %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Structured Terminal Forms Language
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		Development/Other
Url:		http://www.clifford.at/stfl/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ncursesw-devel
BuildRequires:	swig
BuildRequires:	perl-devel, ruby-devel
%py_requires -d
 
%description
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and
Ruby. Since the API is only 14 simple function calls big and there are
already generic SWIG bindings, it is very easy to port STFL to
other scripting languages.

A special language (the Structured Terminal Forms Language) is used to
describe STFL GUIs. The language is designed to be easy and fast to
write so an application programmer does not need to spend ages
fiddling around with the GUI and can concentrate on the more
interesting programming tasks.

%package -n %{libname}
Summary:    Structured Terminal Forms Language library
Group:	    System/Libraries

%description -n %{libname}
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and
Ruby. Since the API is only 14 simple function calls big and there are
already generic SWIG bindings, it is very easy to port STFL to
other scripting languages.

A special language (the Structured Terminal Forms Language) is used to
describe STFL GUIs. The language is designed to be easy and fast to
write so an application programmer does not need to spend ages
fiddling around with the GUI and can concentrate on the more
interesting programming tasks.

This package contains the shared library required for running programs
that use STFL.

%package -n %{develname}
Summary:    Structured Terminal Forms Language development files
Group:	    Development/C
Requires:   %{libname} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and
Ruby. Since the API is only 14 simple function calls big and there are
already generic SWIG bindings, it is very easy to port STFL to
other scripting languages.

A special language (the Structured Terminal Forms Language) is used to
describe STFL GUIs. The language is designed to be easy and fast to
write so an application programmer does not need to spend ages
fiddling around with the GUI and can concentrate on the more
interesting programming tasks.

This package contains the C headers and other files needed to compile
programs that use STFL.

%package -n python-%{name}
Summary:    Structured Terminal Forms Language Python bindings
Group:	    Development/Python
Requires:   libncursesw5
Requires:   python

%description -n python-%{name}
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and
Ruby. Since the API is only 14 simple function calls big and there are
already generic SWIG bindings, it is very easy to port STFL to
other scripting languages.

A special language (the Structured Terminal Forms Language) is used to
describe STFL GUIs. The language is designed to be easy and fast to
write so an application programmer does not need to spend ages
fiddling around with the GUI and can concentrate on the more
interesting programming tasks.

This package contains the bindings needed to use STFL with Python.

%package -n perl-%{name}
Summary:    Structured Terminal Forms Language Perl bindings
Group:	    Development/Perl
Requires:   libncursesw5
Requires:   perl

%description -n perl-%{name}
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and
Ruby. Since the API is only 14 simple function calls big and there are
already generic SWIG bindings, it is very easy to port STFL to
other scripting languages.

A special language (the Structured Terminal Forms Language) is used to
describe STFL GUIs. The language is designed to be easy and fast to
write so an application programmer does not need to spend ages
fiddling around with the GUI and can concentrate on the more
interesting programming tasks.

This package contains the bindings needed to use STFL with Perl.

%package -n ruby-%{name}
Summary:    Structured Terminal Forms Language Ruby bindings
Group:	    Development/Ruby
Requires:   libncursesw5
Requires:   ruby

%description -n ruby-%{name}
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and
Ruby. Since the API is only 14 simple function calls big and there are
already generic SWIG bindings, it is very easy to port STFL to
other scripting languages.

A special language (the Structured Terminal Forms Language) is used to
describe STFL GUIs. The language is designed to be easy and fast to
write so an application programmer does not need to spend ages
fiddling around with the GUI and can concentrate on the more
interesting programming tasks.

This package contains the bindings needed to use STFL with Ruby.

%prep
%setup -q
%{__sed} -i 's,$(prefix)/lib,/%{_libdir},g' python/Makefile.snippet
%{__sed} -i 's,$(prefix)/lib,/%{_libdir},g' ruby/Makefile.snippet
%{__sed} -i 's,sitedir=$(prefix)/$(libdir)/ruby,sitedir=%{_libdir}/ruby/site_ruby,g' ruby/Makefile.snippet
%{__sed} -i 's,libdir=lib,libdir=%{_libdir},g' Makefile 
%{__sed} -i "s,cd python && python -c 'import stfl',python -mcompileall .," python/Makefile.snippet
%{__sed} -i 's,export prefix ?= /usr/local,export prefix ?= %{_prefix},g' Makefile.cfg
%{__sed} -i 's,mkdir -p \$(DESTDIR)\$(prefix)/lib/pkgconfig,mkdir -p \$(DESTDIR)%{_libdir}/pkgconfig,g' Makefile
%{__sed} -i 's,libstfl.a \$(DESTDIR)\$(prefix)/lib/,libstfl.a \$(DESTDIR)%{_libdir},g' Makefile
%{__sed} -i 's,stfl.pc \$(DESTDIR)\$(prefix)/lib/pkgconfig/,stfl.pc \$(DESTDIR)%{_libdir}\/pkgconfig/,g' Makefile

%build
%make

%install
%__rm -rf %{buildroot}
make prefix=%{_prefix} libdir=%{_lib} DESTDIR=%{buildroot} install
%__rm -rf %{buildroot}%{_libdir}/perl5/5.10.0

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING README 
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n python-%{name}
%defattr(-,root,root)
%{py_platsitedir}/*

%files -n perl-%{name}
%defattr(-,root,root)
%{_usr}/lib/perl5/*

%files -n ruby-%{name}
%defattr(-,root,root)
%{_libdir}/ruby/*
