Name:        nspr
Version:     4.15
Release:     15
License:     MPL-2.0
Summary:     Netscape Portable Runtime Library
Group:       libs
URL:         http://www.mozilla.org/projects/nspr/
Source0:     https://ftp.mozilla.org/pub/nspr/releases/v4.15/src/nspr-4.15.tar.gz


BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32


%description
Netscape Portable Runtime library is a platform-neutral API for system level
and libc-like functions.

%package dev
Summary:      Netscape Portable Runtime Library - Development files
Group:        devel/libraries
Requires:     perl
Requires:     nspr = %{version}-%{release}

%description dev
Netscape Portable Runtime Library. This package contains symbolic links,
header files and related items necessary for software development.

%package dev32
Summary:      Netscape Portable Runtime Library - Development files
Group:        devel/libraries
Requires:     perl
Requires:     nspr = %{version}-%{release}
Requires:     nspr-dev

%description dev32
Netscape Portable Runtime Library. This package contains symbolic links,
header files and related items necessary for software development.
%package lib32
Summary:      Netscape Portable Runtime Library - Development files
Group:        devel/libraries
Requires:     perl
Requires:     nspr = %{version}-%{release}

%description lib32
Netscape Portable Runtime Library. This package contains symbolic links,
header files and related items necessary for software development.

%prep
%setup -q -n nspr-%{version}/nspr
# disables installing the static libraries
sed -i 's#$(LIBRARY) ##' config/rules.mk

pushd ..
cp -a nspr build32
popd

%build
CC=gcc

%configure --disable-debug \
 --enable-optimize \
 --enable-64bit --target=x86_64-generic-linux-gnu

%make_build

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-debug \
 --enable-optimize --enable-32bit \
 --disable-64bit --target=i686-generic-linux-gnu --libdir=/usr/lib32

%make_build
popd

%install

pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
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

%files dev32
/usr/lib32/pkgconfig/nspr.pc
/usr/lib32/pkgconfig/32nspr.pc

%files lib32
/usr/lib32/libnspr4.so
/usr/lib32/libplc4.so
/usr/lib32/libplds4.so
