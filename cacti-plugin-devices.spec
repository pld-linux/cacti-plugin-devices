%define		namesrc	devices
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Devices
Summary(pl):	Wtyczka do Cacti - Devices
Name:		cacti-plugin-devices
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://wotsit.thingy.com/haj/cacti/%{namesrc}-%{version}.zip
# Source0-md5:	c2464ec843cc6d3d464ca179cb4b053a
URL:		http://wotsit.thingy.com/haj/cacti/devices-plugin.html
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
This is a simple plugin for the Cacti Plugin Architecture for Cacti
0.8.x. Wanted a tab to show the current availability of his devices,
but without the ability to edit the devices. This is a hacked up copy
of the 'hosts.php' page that forms the Devices page within the
console. All the editing code is removed, and the device devices go to
the Graph Preview mode, with that device as the filter (so you see
only that device's graphs).

%description -l pl
To jest prosta wtyczka dla architektury wtyczek Cacti dla Cacti 0.8.x.
Ma byæ zak³adk± pokazuj±c± aktualn± dostêpno¶æ urz±dzeñ, ale bez
mo¿liwo¶ci edycji urz±dzeñ. Jest to zmodyfikowana kopia strony
'hosts.php' tworz±cej stronê Devices wewn±trz konsoli. Ca³y kod do
modyfikacji ustawieñ zosta³ usuniêty, a urz±dzenie przechodzi do
trybu podgl±du wykresu (Graph Preview) z ustawionym tym urz±dzeniem
jako filtrem (wiêc widaæ tylko wykres dla tego urz±dzenia).

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc LICENSE README 
%{webcactipluginroot}
