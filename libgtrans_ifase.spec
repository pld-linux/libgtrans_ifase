Summary:	Database Access Library
Name:		libgtrans_ifase
Version:	0.2.0
Release:	1
License:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	http://download.sourceforge.net/gtranscript/%{name}-%{version}.tar.gz
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_sysconfdir	/etc

%description
libgtrans_ifase is the library that provides GNOME Transcript with
database access via plugin system.

%package devel
Summary:	Header files for libgtrans_ifase
Summary(pl):	Pliki nag³ówkowe do libgtrans_ifase
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for libgtrans_ifase.

%description -l pl devel
Pliki nag³ówkowe do libgtrans_ifase.

%package static
Summary:	Static libgtrans_ifase library
Summary(pl):	Biblioteka statyczna libgtrans_ifase
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libgtrans_ifase library.

%description -l pl static
Biblioteka statyczna libgtrans_ifase.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_includedir}/gtrans_ifase
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
