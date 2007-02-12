Summary:	Database Access Library
Summary(pl.UTF-8):   Biblioteka dostępu do Baz Danych
Name:		libgtrans_ifase
Version:	0.2.0
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtranscript/%{name}-%{version}.tar.gz
# Source0-md5:	3cd934113478c43d79a8af06be777d44
URL:		http://gtranscript.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgtrans_ifase is the library that provides GNOME Transcript with
database access via plugin system.

%description -l pl.UTF-8
libgtrans_ifase jest biblioteką dostarczającą GNOME Transcript z
dostępem do baz danych poprzez system wtyczek.

%package devel
Summary:	Header files for libgtrans_ifase
Summary(pl.UTF-8):   Pliki nagłówkowe do libgtrans_ifase
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgtrans_ifase.

%description devel -l pl.UTF-8
Pliki nagłówkowe do libgtrans_ifase.

%package static
Summary:	Static libgtrans_ifase library
Summary(pl.UTF-8):   Biblioteka statyczna libgtrans_ifase
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgtrans_ifase library.

%description static -l pl.UTF-8
Biblioteka statyczna libgtrans_ifase.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/gtrans_ifase
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
