Summary:	Database Access Library
Summary(pl):	Biblioteka dostЙpu do Baz Danych
Name:		libgtrans_ifase
Version:	0.2.0
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://download.sourceforge.net/pub/sourceforge/gtranscript/%{name}-%{version}.tar.gz
URL:		http://gtranscript.sourceforge.net/
BuildRequires:	glib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_sysconfdir	/etc

%description
libgtrans_ifase is the library that provides GNOME Transcript with
database access via plugin system.

%description -l pl
libgtrans_ifase jest bibliotek╠ dostarczaj╠c╠ GNOME Transcript z
dostЙpem do baz danych poprzez system wtyczek.

%package devel
Summary:	Header files for libgtrans_ifase
Summary(pl):	Pliki nagЁСwkowe do libgtrans_ifase
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Header files for libgtrans_ifase.

%description -l pl devel
Pliki nagЁСwkowe do libgtrans_ifase.

%package static
Summary:	Static libgtrans_ifase library
Summary(pl):	Biblioteka statyczna libgtrans_ifase
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static libgtrans_ifase library.

%description -l pl static
Biblioteka statyczna libgtrans_ifase.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
