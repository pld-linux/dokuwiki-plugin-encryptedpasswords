%define		plugin		encryptedpasswords
Summary:	DokuWiki Encrypted Passwords Plugin
Summary(pl.UTF-8):	Wtyczka szyfrowania haseł dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20120706
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.werbeagentur-willers.de/download/dokuwiki-plugins/encryptedpasswords.zip
# Source0-md5:	049ab5cd52392ab32c4deb97d84c7cf5
URL:		https://www.dokuwiki.org/plugin:encryptedpasswords
Requires:	dokuwiki >= 20110525
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin let you store 256 bit AES encrypted passwords in your
DokuWiki pages. The password can be decrypted by clicking them
(Javascript must be enabled).

%prep
%setup -q -n %{plugin}
version=$(cat version)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc version
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/*.png
%{plugindir}/version
%dir %{plugindir}/lang
%lang(en) %{plugindir}/lang/en
%lang(de) %{plugindir}/lang/de
