Name:        nspr
Version:     4.28
Release:     30
License:     MPL-2.0
Summary:     Netscape Portable Runtime Library
Group:       libs
URL:         http://www.mozilla.org/projects/nspr/
Source0:     https://ftp.mozilla.org/pub/nspr/releases/v4.28/src/nspr-4.28.tar.gz
Requires: nspr-license = %{version}-%{release}
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
Requires:     nspr-lib32 = %{version}-%{release}
Requires:     nspr-dev = %{version}-%{release}

%description dev32
Netscape Portable Runtime Library. This package contains symbolic links,
header files and related items necessary for software development.

%package lib32
Summary:      Netscape Portable Runtime Library - Development files
Group:        devel/libraries
Requires:     perl
Requires:     nspr-license = %{version}-%{release}
Requires:     nspr = %{version}-%{release}

%description lib32
Netscape Portable Runtime Library. This package contains symbolic links,
header files and related items necessary for software development.

%package license
Summary: license components for the nspr package.
Group: Default

%description license
license components for the nspr package.


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
 --enable-64bit \
 --target=x86_64-generic-linux-gnu

%make_build

pushd ../build32
export CFLAGS="$CFLAGS -m32 -mstackrealign"
export LDFLAGS="$LDFLAGS -m32 -mstackrealign"
export CXXFLAGS="$CXXFLAGS -m32 -mstackrealign"
%configure --disable-debug \
 --enable-optimize \
 --enable-32bit \
 --disable-64bit \
 --target=i686-generic-linux-gnu \
 --libdir=/usr/lib32

%make_build
popd

%install
install -Dm644 LICENSE %{buildroot}/usr/share/package-licenses/nspr/LICENSE
pushd ../build32
%make_install32
if [ -d %{buildroot}/usr/lib32/pkgconfig ]; then
  pushd %{buildroot}/usr/lib32/pkgconfig
  for i in *.pc; do
    ln -s $i 32$i;
  done
  popd
fi
popd
%make_install

%files
/usr/lib64/libnspr4.so
/usr/lib64/libplc4.so
/usr/lib64/libplds4.so

%files dev
/usr/bin/compile-et.pl
/usr/bin/nspr-config
/usr/bin/prerr.properties
/usr/include/md/_aix32.cfg
/usr/include/md/_aix64.cfg
/usr/include/md/_bsdi.cfg
/usr/include/md/_darwin.cfg
/usr/include/md/_freebsd.cfg
/usr/include/md/_hpux32.cfg
/usr/include/md/_hpux64.cfg
/usr/include/md/_linux.cfg
/usr/include/md/_netbsd.cfg
/usr/include/md/_nto.cfg
/usr/include/md/_openbsd.cfg
/usr/include/md/_os2.cfg
/usr/include/md/_qnx.cfg
/usr/include/md/_riscos.cfg
/usr/include/md/_scoos.cfg
/usr/include/md/_solaris.cfg
/usr/include/md/_unixware.cfg
/usr/include/md/_unixware7.cfg
/usr/include/md/_win95.cfg
/usr/include/md/_winnt.cfg
/usr/include/nspr.h
/usr/include/obsolete/pralarm.h
/usr/include/obsolete/probslet.h
/usr/include/obsolete/protypes.h
/usr/include/obsolete/prsem.h
/usr/include/plarena.h
/usr/include/plarenas.h
/usr/include/plbase64.h
/usr/include/plerror.h
/usr/include/plgetopt.h
/usr/include/plhash.h
/usr/include/plstr.h
/usr/include/pratom.h
/usr/include/prbit.h
/usr/include/prclist.h
/usr/include/prcmon.h
/usr/include/prcountr.h
/usr/include/prcpucfg.h
/usr/include/prcvar.h
/usr/include/prdtoa.h
/usr/include/prenv.h
/usr/include/prerr.h
/usr/include/prerror.h
/usr/include/prinet.h
/usr/include/prinit.h
/usr/include/prinrval.h
/usr/include/prio.h
/usr/include/pripcsem.h
/usr/include/private/pprio.h
/usr/include/private/pprthred.h
/usr/include/private/prpriv.h
/usr/include/prlink.h
/usr/include/prlock.h
/usr/include/prlog.h
/usr/include/prlong.h
/usr/include/prmem.h
/usr/include/prmon.h
/usr/include/prmwait.h
/usr/include/prnetdb.h
/usr/include/prolock.h
/usr/include/prpdce.h
/usr/include/prprf.h
/usr/include/prproces.h
/usr/include/prrng.h
/usr/include/prrwlock.h
/usr/include/prshm.h
/usr/include/prshma.h
/usr/include/prsystem.h
/usr/include/prthread.h
/usr/include/prtime.h
/usr/include/prtpool.h
/usr/include/prtrace.h
/usr/include/prtypes.h
/usr/include/prvrsion.h
/usr/include/prwin16.h
/usr/lib64/pkgconfig/nspr.pc
/usr/share/aclocal/nspr.m4

%files dev32
/usr/lib32/pkgconfig/nspr.pc
/usr/lib32/pkgconfig/32nspr.pc

%files lib32
/usr/lib32/libnspr4.so
/usr/lib32/libplc4.so
/usr/lib32/libplds4.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nspr/LICENSE
