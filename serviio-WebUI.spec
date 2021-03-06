%define commit 2fe4e73fde55cc2cc6ffc23e0d40c4dd09580c66

Name:		serviio-WebUI
Version:	1.6.3
Release:	3%{?dist}
License:	Free to use, see README.txt included in serviio-WebUI documentation
Summary:	A web user interface for the serviio media server
URL:		https://github.com/SwoopX/Web-UI-for-Serviio
Group:		Productivity/Multimedia/Other
Source:		%{commit}.zip
Patch1:		logs.php.patch
Patch2:		library.php.patch
Patch3:		messages_en.properties.patch
Patch4:		messages_de.properties.patch
BuildRequires:	unzip tar gzip
Requires:   	serviio >= 1.5
Requires:	php-mbstring
BuildRoot:  	%{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch

%description
It allows you to stream your media files (music, video 
or images) to renderer devices (e.g. a TV set, Bluray player, games console
or mobile phone) on your connected home network.

%prep
%setup -q -n Web-UI-for-Serviio-%{commit}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build


%install
install -d $RPM_BUILD_ROOT/usr/share/serviio-WebUI
cp -R * $RPM_BUILD_ROOT/usr/share/serviio-WebUI
cp -R .htaccess $RPM_BUILD_ROOT/usr/share/serviio-WebUI


%pre


%post


%files
%defattr(-,serviio,serviio)
%doc README.txt
/usr/share/serviio-WebUI



%changelog
* Mon Sep 7 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.6.3-3
- Added dist-tag to releaseversion

* Sat Sep 5 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.6.3-2
- Changed source url to be commit specific in github

* Tue Feb 10 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.6.3
- New upstream release

* Fri Jan 30 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.6.2
- New upstream release

* Wed Jan 21 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.6.1
- New upstream release

* Tue Jan 20 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.6
- New upstream version number (same code)

* Wed Jan 14 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.6-1
- New upstream release for Serviio 1.5

* Sat Nov 15 2014 Fredrik fornstad <fredrik.fornstad@gmail.com> - 1.5.5-1
- New upstream release incl auto NIC selection, auto number of cores selection, corrected licence upload and prep for new Serviio API

* Sat Mar 15 2014 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.4-2
- New upstream bug correction for Iphone switch

* Sun Feb 02 2014 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.4-1
- New upstream release plus correction of index.php to enable Serviidb source by default

* Sat Jan 18 2014 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.3-2
- New upstream release

* Sat Jan 11 2014 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.3-1
- New upstream release, added hint to enable 3rd party app read access for flexshares

* Sat Nov 23 2013 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.2-1
- New upstream release

* Sun Nov 17 2013 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.1-2
- Added and adjusted patches to give user guidance to ClearOS default directories

* Sun Nov 10 2013 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.1-1
- First build for ClearOS 6
