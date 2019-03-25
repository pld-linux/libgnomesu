Summary:	Library for providing superuser privileges
Summary(pl.UTF-8):	Biblioteka do udostępniania uprawnień superużytkownika
Name:		libgnomesu
Version:	1.0.0
Release:	10
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://members.chello.nl/~h.lai/libgnomesu/%{name}-%{version}.tar.gz
# Source0-md5:	9f1cb8c3f61ad2fb31ad05a5d3eb211d
Patch0:		%{name}-xauth-nolookup.patch
Patch1:		%{name}-mainloop.patch
Patch2:		%{name}-unsetenv.patch
Patch3:		%{name}-modernize.patch
Patch4:		%{name}-startup-notification.patch
Patch5:		%{name}-pam-handling.patch
Patch6:		%{name}-drop-libgnomeui.patch
Patch7:		%{name}-safe-path.patch
Patch8:		%{name}-remove-prior-cookie.patch
Patch9:		%{name}-i18n.patch
Patch10:	%{name}-memory-cleaning.patch
Patch11:	%{name}-format.patch
URL:		http://members.chello.nl/~h.lai/libgnomesu/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
Provides:	gnomesu = %{version}-%{release}
Obsoletes:	gnomesu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgnomesu is a library for providing superuser privileges to GNOME
applications. It supports sudo, consolehelper, PAM and su.

This package contains actual gnomesu program and backends.

%description -l pl.UTF-8
libgnomesu to biblioteka do udostępniania uprawnień superużytkownika
aplikacjom GNOME. Obsługuje sudo, consolehelper, PAM i su.

Ten pakiet zawiera właściwy program gnomesu i backendy.

%package libs
Summary:	libgnomesu library itself
Summary(pl.UTF-8):	Sama biblioteka libgnomesu
Group:		X11/Libraries

%description libs
libgnomesu library itself.

%description libs -l pl.UTF-8
Sama biblioteka libgnomesu.

%package devel
Summary:	Headers for libgnomesu
Summary(pl.UTF-8):	Pliki nagłówkowe libgnomesu
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Libraries and include files that you will need to use libgnomesu.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów korzystających z
libgnomesu.

%package static
Summary:	Static libgnomesu libraries
Summary(pl.UTF-8):	Statyczne biblioteki libgnomesu
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomesu libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek libgnomesu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

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

chmod 755 $RPM_BUILD_ROOT%{_libexecdir}/gnomesu*backend

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{sr@Latn,sr@latin}

%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gnomesu-pam
%attr(755,root,root) %{_bindir}/gnomesu
%attr(4755,root,root) %{_libexecdir}/gnomesu-backend
%attr(4755,root,root) %{_libexecdir}/gnomesu-pam-backend
%{_datadir}/application-registry/gnomesu-nautilus.applications
%{_datadir}/mime-info/gnomesu-nautilus.keys

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomesu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomesu.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/api.html doc/libgnomesu.css
%attr(755,root,root) %{_libdir}/libgnomesu.so
%{_libdir}/libgnomesu.la
%{_includedir}/libgnomesu-1.0
%{_pkgconfigdir}/libgnomesu-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomesu.a
