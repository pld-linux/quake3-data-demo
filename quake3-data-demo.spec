Summary:	Quake III Arena - demo data files
Summary(pl.UTF-8):	Quake III Arena - pliki danych w wersji demo
Name:		quake3-data-demo
Version:	1.11.6
Release:	1
License:	Q3A EULA (non-commercially distributable)
Group:		Applications/Games
Source0:	ftp://ftp.idsoftware.com/idstuff/quake3/linux/linuxq3ademo-1.11-6.x86.gz.sh
# Source0-md5:	484610c1ce34272223a52ec331c99d5d
URL:		http://www.quake3arena.com/
Requires:	quake3-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quake III Arena - demo data files.

%description -l pl.UTF-8
Quake III Arena - pliki danych w wersji demo.

%prep
%setup -q -c -T
tail -n +165 %{SOURCE0} | tar xzf -
chmod u+w -R .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/quake3/baseq3

install demoq3/pak0.pk3 $RPM_BUILD_ROOT%{_datadir}/games/quake3/baseq3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Q3A_EULA.txt
%{_datadir}/games/quake3/baseq3/pak0.pk3
