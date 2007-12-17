%undefine __find_provides
%undefine __find_requires

Summary:	French sound files for the Asterisk PBX and telephony application and toolkit
Name:		asterisk-core-sounds-fr
Version:	1.4.5
Release:	%mkrel 2
License:	BSD
Group:		System/Servers
URL:		http://www.asterisk.org/
Source0:	http://ftp.digium.com/pub/telephony/sounds/%{name}-alaw-%{version}.tar.gz
Source1:	http://ftp.digium.com/pub/telephony/sounds/%{name}-g722-%{version}.tar.gz
Source2:	http://ftp.digium.com/pub/telephony/sounds/%{name}-g729-%{version}.tar.gz
Source3:	http://ftp.digium.com/pub/telephony/sounds/%{name}-gsm-%{version}.tar.gz
Source4:	http://ftp.digium.com/pub/telephony/sounds/%{name}-ulaw-%{version}.tar.gz
Source5:	http://ftp.digium.com/pub/telephony/sounds/%{name}-wav-%{version}.tar.gz
Requires:	asterisk
Requires:	locales-fr
Provides:	asterisk-core-sounds
Conflicts:	asterisk-core-sounds-es asterisk-core-sounds-en
BuildArch:	noarch

%description
Asterisk is an Open Source PBX and telephony development platform that can both
replace a conventional PBX and act as a platform for developing custom
telephony applications for delivering dynamic content over a telephone
similarly to how one can deliver dynamic content through a web browser using
CGI and a web server.
 
Asterisk talks to a variety of telephony hardware including BRI, PRI, POTS, and
IP telephony clients using the Inter-Asterisk eXchange protocol (e.g. gnophone
or miniphone).

This package contains freely usable recorded sounds that were meant to be used
with Asterisk in the following formats: a-Law, G.722, G.729, GSM, mu-Law, WAV

%prep

%setup -q -c -T -n asterisk-core-sounds-%{version} -a0 -a1 -a2 -a3 -a4 -a5

# fix dir perms
find . -type d | xargs chmod 755
    
# fix file perms
find . -type f | xargs chmod 644

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_localstatedir}/asterisk/sounds

cp -aRf * %{buildroot}%{_localstatedir}/asterisk/sounds/

# cleanup
rm -f %{buildroot}%{_localstatedir}/asterisk/sounds/CREDITS-asterisk-core-*-%{version}

# make a file list
find %{buildroot}%{_localstatedir}/asterisk/sounds -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0644,root,root) /' >> %{name}.filelist

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.filelist
%defattr(-,root, root)
%doc CREDITS-asterisk-core-*-%{version}

