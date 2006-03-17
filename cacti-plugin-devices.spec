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
Plugin for Cacti -This is a simple plugin for the Cacti Plugin 
Architecture for Cacti 0.8.x.
Wanted a tab to show the current availability of his devices,
but without the ability to edit the devices. This is a hacked up copy
of the 'hosts.php' page that forms the Devices page within the console.
All the editing code is removed, and the device devices go to the Graph
Preview mode, with that device as the filter (so you see only that
device's graphs).


%description -l pl
Wtyczka do Cacti - 

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
