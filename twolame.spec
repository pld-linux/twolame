Summary:	Optimized MPEG Audio Layer 2 (MP2) encoder
Summary(pl):	Zoptymalizowany koder MPEG Audio Layer 2 (MP2)
Name:		twolame
Version:	0.3.9
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/twolame/%{name}-%{version}.tar.gz
# Source0-md5:	79be2e6c99495c767d037b977a32eab5
URL:		http://www.twolame.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libtool
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

%description -l pl
TwoLAME to zoptymalizowany koder MPEG Audio Layer 2 (MP2) oparty na
tooLAME Mike'a Chenga, kt�ry z kolei jest oparty na kodzie ISO dist10
i fragmentach LAME.

Cechy dodane do TwoLAME:
 - pe�na zgodno�� z w�tkami
 - statyczna i wsp�dzielona biblioteka (libtwolame)
 - API bardzo podobne do API LAME (dla �atwego portowania)
 - zgodno�� z C99
 - frontend obs�uguje wiele rodzaj�w plik�w wej�ciowych (poprzez
   libsndfile)

%package libs
Summary:	TwoLAME MP2 encoding library
Group:		Libraries

%description libs
TwoLAME MP2 encoding library.

%package devel
Summary:	Header files for TwoLAME library
Summary(pl):	Pliki nag��wkowe biblioteki TwoLAME
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for TwoLAME library.

%description devel -l pl
Pliki nag��wkowe biblioteki TwoLAME.

%package static
Summary:	Static TwoLAME library
Summary(pl):	Statyczna biblioteka TwoLAME
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static TwoLAME library.

%description static -l pl
Statyczna biblioteka TwoLAME.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/twolame

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
