%define	nspr_version	4.6
%define	nspr_evr	1:%{nspr_version}
%define	nss_version	3.11
%define	nss_evr		1:%{nss_version}
Summary:	svrcore - development files for secure PIN handling using NSS crypto
Summary(pl):	svrcore - pliki programistyczne do bezpiecznej obs³ugi PIN-ów przy u¿yciu NSS
Name:		svrcore-devel
Version:	4.0.2
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Development/Libraries
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/directory/svrcore/releases/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	62cb9c16133a979828f4494bd67223c1
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
svrcore udostêpnia aplikacjom kilka sposobów obs³ugi bezpiecznego
przechowywania PIN-ów, np. w aplikacji, która musi byæ zrestartowana,
ale wymaga PIN-u do odblokowania klucza prywatnego i innych danych
kryptograficznych bez interwencji u¿ytkownika. svrcore wykorzystuje
funkcje udostêpniane przez bibliotekê NSS.

%prep
%setup -q

%build
%{__make} -C mozilla/security/coreconf \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"
%{__make} -C mozilla/security/svrcore \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I. -I/usr/include/nspr -I/usr/include/nss"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/svrcore,%{_pkgconfigdir}}
install mozilla/dist/public/svrcore/*.h $RPM_BUILD_ROOT%{_includedir}/svrcore
install mozilla/dist/*.OBJ/lib/libsvrcore.a $RPM_BUILD_ROOT%{_libdir}
sed mozilla/security/svrcore/svrcore.pc.in -e "
	s,%%libdir%%,%{_libdir},g
	s,%%prefix%%,%{_prefix},g
	s,%%exec_prefix%%,%{_prefix},g
	s,%%includedir%%,%{_includedir}/svrcore,g
	s,%%NSPR_VERSION%%,%{nspr_version},g
	s,%%NSS_VERSION%%,%{nss_version},g
	s,%%SVRCORE_VERSION%%,%{svrcore_version},g
" > $RPM_BUILD_ROOT%{_pkgconfigdir}/svrcore.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc mozilla/security/svrcore/{LICENSE,README}
%{_libdir}/libsvrcore.a
%{_includedir}/svrcore
%{_pkgconfigdir}/svrcore.pc
