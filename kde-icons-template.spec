#$Revision: 1.4 $, $Date: 2003-08-18 08:08:13 $

%define         _name

Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:
Release:	1
License:	GPL
Group:		Themes
Source0:	%{_name}-%{version}.tar.bz2
# Source0-md5:
URL:
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

%description
%{_name} is

%description -l pl
%{_name} to motyw ikon

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xjf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/
