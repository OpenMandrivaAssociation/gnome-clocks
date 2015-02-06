%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Clocks applications for GNOME
Name:		gnome-clocks
Version:	0.1.5
Release:	2
License:	GPLv2+
Group:		Development/Other
URL:		http://live.gnome.org/Clocks
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	python-setuptools
BuildRequires:	pythonegg(python-distutils-extra)

%description
Clock application designed for GNOME 3.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%doc COPYING README NEWS
%{python_sitelib}/*
%{_bindir}/%{name}
%{_datadir}/%{name}/

