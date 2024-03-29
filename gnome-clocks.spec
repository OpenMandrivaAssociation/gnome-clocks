%define _disable_rebuild_configure 1

%define url_ver %(echo %{version}|cut -d. -f1,2)
%define busname org.gnome.clocks

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Summary:	Clocks applications for GNOME
Name:		gnome-clocks
Version:	46.0
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		https://live.gnome.org/Clocks
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-2.0) >= 2.30.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.36
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(gweather4)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:	pkgconfig(gnome-desktop-3.0) >= 3.7.90
BuildRequires:	pkgconfig(libnotify) >= -.7.0
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(geoclue-2.0)
BuildRequires:	pkgconfig(geocode-glib-2.0)
BuildRequires:	pkgconfig(gsound)
BuildRequires:	vala-tools
BuildRequires:	libxml2-utils
BuildRequires:	itstool
BuildRequires:	meson


%description
Clock application designed for GNOME 3.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README.md
%{_bindir}/%{name}
#{_datadir}/%{name}
%{_datadir}/metainfo/org.gnome.clocks.metainfo.xml
%{_iconsdir}/*/*/apps/*.*
%{_datadir}/applications/%{busname}.desktop
%{_datadir}/glib-2.0/schemas/%{busname}.gschema.xml
%{_datadir}/dbus-1/services/%{busname}.service
%{_datadir}/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini
