%define	nspr_version	4.6.4
%define	nspr_evr	1:%{nspr_version}
%define	nss_version	3.11.4
%define	nss_evr		1:%{nss_version}
Summary:	svrcore library for secure PIN handling using NSS crypto
Summary(pl):	Biblioteka svrcore do bezpiecznej obs�ugi PIN-�w przy u�yciu NSS
Name:		svrcore
Version:	4.0.3.01
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Development/Libraries
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/directory/svrcore/releases/4.0.3/%{name}-%{version}.tar.gz
# Source0-md5:	fbb56acf580aa0ebb32df58594458b28
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

%description -l pl
svrcore udost�pnia aplikacjom kilka sposob�w obs�ugi bezpiecznego
przechowywania PIN-�w, np. w aplikacji, kt�ra musi by� zrestartowana,
ale wymaga PIN-u do odblokowania klucza prywatnego i innych danych
kryptograficznych bez interwencji u�ytkownika. svrcore wykorzystuje
funkcje udost�pniane przez bibliotek� NSS.

%package devel
Summary:	Header files for svrcore library
Summary(pl):	Pliki nag��wkowe biblioteki svrcore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	nspr-devel >= %{nspr_evr}
Requires:	nss-devel >= %{nss_evr}

%description devel
Header files for svrcore library.

%description devel -l pl
Pliki nag��wkowe biblioteki svrcore.

%package static
Summary:	Static svrcore library
Summary(pl):	Statyczna biblioteka svrcore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static svrcore library.

%description static -l pl
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvrcore.so.*.*.*
%{_libdir}/libsvrcore.la
%{_includedir}/svrcore.h
%{_pkgconfigdir}/svrcore.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsvrcore.a
