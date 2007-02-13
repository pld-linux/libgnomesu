# TODO: separate -libs: suid binaries are not needed for -devel
Summary:	Library for providing superuser privileges
Summary(pl.UTF-8):	Biblioteka do udostępnianai uprawnień superużytkownika
Name:		libgnomesu
Version:	0.9.5
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomesu/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	0232d1356c9c12327e8729495fb4f9a0
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgnomesu is a library for providing superuser privileges to GNOME
applications. It supports sudo, consolehelper, PAM and su.

%description -l pl.UTF-8
libgnomesu to biblioteka do udostępniania uprawnień superużytkownika
aplikacjom GNOME. Obsługuje sudo, consolehelper, PAM i su.

%package devel
Summary:	Headers for libgnomesu
Summary(pl.UTF-8):	Pliki nagłówkowe libgnomesu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and include files that you will need to use libgnomesu.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów korzystających z
libgnomesu.

%package static
Summary:	Static libgnomesu libraries
Summary(pl.UTF-8):	Statyczne biblioteki libgnomesu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomesu libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek libgnomesu.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install \
	--disable-setuid-error \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT%{_libdir}/gnomesu*backend

%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gnomesu-pam
%attr(755,root,root) %{_bindir}/gnomesu
%attr(4755,root,root) %{_libdir}/gnomesu-backend
%attr(4755,root,root) %{_libdir}/gnomesu-pam-backend
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/application-registry/*.applications
%{_datadir}/mime-info/*.keys

%files devel
%defattr(644,root,root,755)
%doc doc/api.html doc/libgnomesu.css
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libgnomesu-1.0

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
