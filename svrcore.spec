%define	nspr_version	4.6.4
%define	nspr_evr	1:%{nspr_version}
%define	nss_version	3.11.4
%define	nss_evr		1:%{nss_version}
Summary:	svrcore library for secure PIN handling using NSS crypto
Summary(pl.UTF-8):	Biblioteka svrcore do bezpiecznej obsługi PIN-ów przy użyciu NSS
Name:		svrcore
Version:	4.0.4
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Development/Libraries
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/directory/svrcore/releases/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	46bcdc82624d11c1bb168cf9f15e066c
URL:		http://www.mozilla.org/directory/
BuildRequires:	nspr-devel >= %{nspr_evr}
BuildRequires:	nss-devel >= %{nss_evr}
BuildRequires:	perl-base
Requires:	nspr >= %{nspr_evr}
Requires:	nss >= %{nss_evr}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
svrcore provides applications with several ways to handle secure PIN
storage e.g. in an application that must be restarted, but needs the
PIN to unlock the private key and other crypto material, without user
intervention. svrcore uses the facilities provided by NSS.

%description -l pl.UTF-8
svrcore udostępnia aplikacjom kilka sposobów obsługi bezpiecznego
przechowywania PIN-ów, np. w aplikacji, która musi być zrestartowana,
ale wymaga PIN-u do odblokowania klucza prywatnego i innych danych
kryptograficznych bez interwencji użytkownika. svrcore wykorzystuje
funkcje udostępniane przez bibliotekę NSS.

%package devel
Summary:	Header files for svrcore library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki svrcore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	nspr-devel >= %{nspr_evr}
Requires:	nss-devel >= %{nss_evr}

%description devel
Header files for svrcore library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki svrcore.

%package static
Summary:	Static svrcore library
Summary(pl.UTF-8):	Statyczna biblioteka svrcore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static svrcore library.

%description static -l pl.UTF-8
Statyczna biblioteka svrcore.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_libdir}/libsvrcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsvrcore.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvrcore.so
%{_libdir}/libsvrcore.la
%{_includedir}/svrcore.h
%{_pkgconfigdir}/svrcore.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsvrcore.a
