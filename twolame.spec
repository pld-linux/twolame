Summary:	Optimized MPEG Audio Layer 2 (MP2) encoder
Summary(pl.UTF-8):	Zoptymalizowany koder MPEG Audio Layer 2 (MP2)
Name:		twolame
Version:	0.3.13
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/twolame/%{name}-%{version}.tar.gz
# Source0-md5:	4113d8aa80194459b45b83d4dbde8ddb
URL:		http://www.twolame.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder based on
tooLAME by Mike Cheng, which in turn is based upon the ISO dist10 code
and portions of LAME.

Features added to TwoLAME:
 - Fully thread-safe
 - Static and shared library (libtwolame)
 - API very similar to LAME's (for easy porting)
 - C99 compliant
 - Frontend supports wider range of input files (using libsndfile)

%description -l pl.UTF-8
TwoLAME to zoptymalizowany koder MPEG Audio Layer 2 (MP2) oparty na
tooLAME Mike'a Chenga, który z kolei jest oparty na kodzie ISO dist10
i fragmentach LAME.

Cechy dodane do TwoLAME:
 - pełna zgodność z wątkami
 - statyczna i współdzielona biblioteka (libtwolame)
 - API bardzo podobne do API LAME (dla łatwego portowania)
 - zgodność z C99
 - frontend obsługuje wiele rodzajów plików wejściowych (poprzez
   libsndfile)

%package libs
Summary:	TwoLAME MP2 encoding library
Summary(pl.UTF-8):	Biblioteka kodująca MP2
Group:		Libraries
Conflicts:	twolame < 0.3.9

%description libs
TwoLAME MP2 encoding library.

%description libs -l pl.UTF-8
Biblioteka kodująca MP2.

%package devel
Summary:	Header files for TwoLAME library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki TwoLAME
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for TwoLAME library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki TwoLAME.

%package static
Summary:	Static TwoLAME library
Summary(pl.UTF-8):	Statyczna biblioteka TwoLAME
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static TwoLAME library.

%description static -l pl.UTF-8
Statyczna biblioteka TwoLAME.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/twolame

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/twolame
%{_mandir}/man1/twolame.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtwolame.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtwolame.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/libtwolame.so
%{_libdir}/libtwolame.la
%{_includedir}/twolame.h
%{_pkgconfigdir}/twolame.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtwolame.a
