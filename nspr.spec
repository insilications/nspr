Name:        nspr
Version:     4.10.8
Release:     9.6
License:     MPL-2.0
Summary:     Netscape Portable Runtime Library
Group:       libs
URL:         http://www.mozilla.org/projects/nspr/
Source0:     ftp://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v4.10.8/src/nspr-4.10.8.tar.gz

%description
Netscape Portable Runtime library is a platform-neutral API for system level
and libc-like functions.

%package dev
Summary:      Netscape Portable Runtime Library - Development files
Group:        devel/libraries
Requires:     perl
Requires:     %{name} = %{version}-%{release}

%description dev
Netscape Portable Runtime Library. This package contains symbolic links,
header files and related items necessary for software development.

%prep
%setup -q -n %{name}-%{version}/%{name}
# disables installing the static libraries
sed -i 's#$(LIBRARY) ##' config/rules.mk

%build
CC=gcc

%configure --disable-debug \
 --enable-optimize \
 --enable-64bit --target=x86_64-generic-linux-gnu

%make_build

%install
%make_install

%files
%doc LICENSE
%{_libdir}/libnspr4.so
%{_libdir}/libplc4.so
%{_libdir}/libplds4.so

%files dev
%{_bindir}/*
%{_includedir}/md/*.cfg
%{_includedir}/*.h
%{_includedir}/obsolete/*.h
%{_includedir}/private/*.h
%{_libdir}/pkgconfig/nspr.pc
%{_datadir}/aclocal/nspr.m4
