Summary:	A Doom level (wad) editor
Name:		yadex
Version:	1.7.0
Release:	0.3
Epoch:		0
License:	GPL v2
Group:		Applications/Games
Source0:	http://www.teaser.fr/~amajorel/yadex/%{name}-%{version}.tar.gz
# Source0-md5:	d341abe066525394082edfd520af86ae
URL:		http://www.teaser.fr/~amajorel/yadex/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sysconfdir /etc/%{name}
%define	_datadir	/usr/share/games/%{name}

%description
Yadex is a Doom level (wad) editor for Unix systems running X,
including Linux. It supports Doom alpha, Doom beta, Doom, Ultimate
Doom, Final Doom, Doom II, Heretic and also, in a more or less limited
way, Hexen and Strife.

Yadex is descended from DEU 5.21. Therefore, as you might expect, it's
a rather low-level editor that requires you to take care of a lot of
detail but on the flip side allows you to control very precisely what
you are doing. In addition, it has many advanced functions that DEU
didn't have, to make certain tedious tasks easy.

%prep
%setup -q

sed -i -e '/iwad/s/local\///' yadex.cfg

%build
# not gnu configure
./configure \
	--prefix %{_prefix} \
	--cc %{__cc} \
	--cxx %{__cxx}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man6,%{_datadir}}

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

install obj/0/yadex $RPM_BUILD_ROOT%{_bindir}
install ygd/* $RPM_BUILD_ROOT%{_datadir}
install doc/yadex.6 $RPM_BUILD_ROOT%{_mandir}/man6
install yadex.cfg $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc CHANGES FAQ README TODO VERSION
%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}
%{_mandir}/man6/*
