%define major	0
# TODO: move to rpm macros
%define	ruby_sitedir %(%{__ruby} -rrbconfig -e 'print Config::CONFIG["sitedir"]')

%define libname   %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Structured Terminal Forms Language
Name:		stfl
Version:	0.21
Release:	6
Source0:	%{name}-%{version}.tar.gz
Patch0:		stfl-0.21-pass-ldflags-and-ldlibs.patch
License:	GPLv3+
Group:		Development/Other
Url:		http://www.clifford.at/stfl/
BuildRequires:	ncursesw-devel
BuildRequires:	swig
BuildRequires:	perl-devel ruby-devel python-devel
 
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

%package -n	%{libname}
Summary:	Structured Terminal Forms Language library
Group:		System/Libraries

%description -n	%{libname}
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

%package -n	%{develname}
Summary:	Structured Terminal Forms Language development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
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

%package -n	python-%{name}
Summary:	Structured Terminal Forms Language Python bindings
Group:		Development/Python
Requires:	python

%description -n	python-%{name}
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

%package -n	perl-%{name}
Summary:	Structured Terminal Forms Language Perl bindings
Group:		Development/Perl

%description -n	perl-%{name}
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

%package -n	ruby-%{name}
Summary:	Structured Terminal Forms Language Ruby bindings
Group:		Development/Ruby
Requires:	ruby

%description -n	ruby-%{name}
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
%patch0 -p1 -b .ldflags~
%{__sed} -i 's,$(prefix)/lib,/%{_libdir},g' python/Makefile.snippet
%{__sed} -i 's,$(prefix)/lib,/%{_libdir},g' ruby/Makefile.snippet
%{__sed} -i 's,$(prefix)/$(libdir)/ruby,%{ruby_sitedir},g' ruby/Makefile.snippet
%{__sed} -i 's,libdir=lib,libdir=%{_libdir},g' Makefile 
%{__sed} -i "s,cd python && python -c 'import stfl',python -mcompileall .," python/Makefile.snippet
%{__sed} -i 's,export prefix ?= /usr/local,export prefix ?= %{_prefix},g' Makefile.cfg
%{__sed} -i 's,mkdir -p \$(DESTDIR)\$(prefix)/lib/pkgconfig,mkdir -p \$(DESTDIR)%{_libdir}/pkgconfig,g' Makefile
%{__sed} -i 's,libstfl.a \$(DESTDIR)\$(prefix)/lib/,libstfl.a \$(DESTDIR)%{_libdir},g' Makefile
%{__sed} -i 's,stfl.pc \$(DESTDIR)\$(prefix)/lib/pkgconfig/,stfl.pc \$(DESTDIR)%{_libdir}\/pkgconfig/,g' Makefile

%build
CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" %make

%install
make prefix=%{_prefix} libdir=%{_lib} DESTDIR=%{buildroot} install

%files -n %{libname}
%{_libdir}/libstfl.so.%{major}*

%files -n %{develname}
%doc COPYING README 
%{_includedir}/stfl.h
%{_libdir}/libstfl.a
%{_libdir}/libstfl.so
%{_libdir}/pkgconfig/stfl.pc

%files -n python-%{name}
# XXX: python extension should likely not be located under this directory..
#%{py_dyndir}/_stfl.so
%dir %{py_platsitedir}/lib-dynload
%{py_platsitedir}/lib-dynload/_stfl.so
%{py_platsitedir}/stfl.py*

%files -n perl-%{name}
%{perl_vendorarch}/example.pl
%{perl_vendorarch}/stfl.pm
%dir %{perl_vendorarch}/auto/stfl
%{perl_vendorarch}/auto/stfl/stfl.so

%files -n ruby-%{name}
%{ruby_sitearchdir}/stfl.so
