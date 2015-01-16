Name:		serviio-WebUI
Version:	1.5.6
Release:	1
License:	Free to use, see README.txt included in serviio-WebUI documentation
Summary:	A web user interface for the serviio media server
URL:		https://github.com/SwoopX/Web-UI-for-Serviio/archive/Serviio-1.5.zip
Group:		Productivity/Multimedia/Other
Source:		Serviio-1.5.zip
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
%setup -q -n Web-UI-for-Serviio-Serviio-1.5
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
