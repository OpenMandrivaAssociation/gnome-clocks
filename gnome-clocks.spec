%define _disable_rebuild_configure 1

%define url_ver %(echo %{version}|cut -d. -f1,2)
%define busname org.gnome.clocks

Summary:	Clocks applications for GNOME
Name:		gnome-clocks
Version:	3.18.0
Release:	2
License:	GPLv2+
Group:		Development/Other
URL:		http://live.gnome.org/Clocks
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
Buildrequires:	pkgconfig(gio-2.0) >= 2.30.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.36
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.9.11
BuildRequires:	pkgconfig(libcanberra) >= 0.30
BuildRequires:	pkgconfig(gweather-3.0) >= 3.9.3
BuildRequires:	pkgconfig(gnome-desktop-3.0) >= 3.7.90
BuildRequires:	pkgconfig(libnotify) >= -.7.0
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(geoclue-2.0)
BuildRequires:	pkgconfig(geocode-glib-1.0)
BuildRequires:	pkgconfig(gsound)
BuildRequires:	vala-tools
BuildRequires:	libxml2-utils
BuildRequires:	itstool

%description
Clock application designed for GNOME 3.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING README NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{busname}.appdata.xml
%{_iconsdir}/*/*/apps/*.png
%{_iconsdir}/hicolor/symbolic/apps/gnome-clocks-symbolic.svg
%{_datadir}/applications/%{busname}.desktop
%{_datadir}/glib-2.0/schemas/%{busname}.gschema.xml
%{_datadir}/dbus-1/services/%{busname}.service
%{_datadir}/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini
