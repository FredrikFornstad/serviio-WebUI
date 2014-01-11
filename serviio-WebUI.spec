Name:		serviio-WebUI
Version:	1.5.3
Release:	1
License:	Free to use, see README.txt included in serviio-WebUI documentation
Summary:	A web user interface for the serviio media server
URL:		https://github.com/SwoopX/Web-UI-for-Serviio/archive/Serviio-1.3.zip
Group:		Productivity/Multimedia/Other
Source:		Serviio-1.4.zip
Patch1:		logs.php.patch
Patch2:		library.php.patch
Patch3:		messages_en.properties.patch
Patch4:		messages_de.properties.patch
BuildRequires:	unzip tar gzip
Requires:   	serviio >= 1.4
Requires:	php-mbstring
BuildRoot:  	%{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch

%description
It allows you to stream your media files (music, video 
or images) to renderer devices (e.g. a TV set, Bluray player, games console
or mobile phone) on your connected home network.

%prep
%setup -q -n Web-UI-for-Serviio-Serviio-1.4
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
* Sat Jan 11 2014 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.3-1
- New upstream release, added hint to enable 3rd party app read access for flexshares

* Sat Nov 23 2013 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.2-1
- New upstream release

* Sun Nov 17 2013 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.1-2
- Added and adjusted patches to give user guidance to ClearOS default directories

* Sun Nov 10 2013 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.1-1
- First build for ClearOS 6
