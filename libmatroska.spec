# For some reasons library is unstripped and we don't have time for investigation
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define ebmlver 1.2.1
%define major 5
%define libname %mklibname matroska %{major}
%define develname %mklibname -d matroska

Summary:	Matroska Audio/Video file format library
Name:		libmatroska
Version:	1.3.0
Release:	3
License:	GPL/QPL
Group:		System/Libraries
URL:		http://www.matroska.org/
Source0:	http://dl.matroska.org/downloads/libmatroska/%name-%version.tar.bz2
BuildRequires:	libebml-devel >= %{ebmlver}

%description
In short, matroska is a new Audio/Video file format. It is an advanced
and full featured format.

Advanced because it is based on EBML, a kind of XML equivalent, that
allow infinite extensibility of the format. And full featured because
it includes precise seeking, any audio/video/subtitle codec support
including VCM/ACM/DirectShow compatibility, timecode based format,
complex frame dependencies, chaptering, internationalisation, error
protection, tagging, file attachement, control track (to be defined),
menu (to be defined), etc. All these features are not yet implemented
but already defined in the format.

%package -n %{libname}
Summary:	Matroska Audio/Video file format shared library
Group:		System/Libraries

%description -n %{libname}
In short, matroska is a new Audio/Video file format. It is an advanced
and full featured format.

Advanced because it is based on EBML, a kind of XML equivalent, that
allow infinite extensibility of the format. And full featured because
it includes precise seeking, any audio/video/subtitle codec support
including VCM/ACM/DirectShow compatibility, timecode based format,
complex frame dependencies, chaptering, internationalisation, error
protection, tagging, file attachement, control track (to be defined),
menu (to be defined), etc. All these features are not yet implemented
but already defined in the format.

%package -n %{develname}
Group:		Development/C++
Summary:	Matroska Audio/Video file format headers and static library
Requires:	%{libname} = %{version}-%{release}
Provides:	libmatroska-devel = %{version}-%{release}

%description -n %{develname}
In short, matroska is a new Audio/Video file format. It is an advanced
and full featured format.

Advanced because it is based on EBML, a kind of XML equivalent, that
allow infinite extensibility of the format. And full featured because
it includes precise seeking, any audio/video/subtitle codec support
including VCM/ACM/DirectShow compatibility, timecode based format,
complex frame dependencies, chaptering, internationalisation, error
protection, tagging, file attachement, control track (to be defined),
menu (to be defined), etc. All these features are not yet implemented
but already defined in the format.

This package contains the C++ headers and the static library needed
for development with Matroska.

%prep
%setup -q
chmod 644 LICENSE*

%build
cd make/linux
%make CXX="g++ %{optflags} %{ldflags}"

%install
cd make/linux
%makeinstall_std prefix=%{buildroot}/%{_prefix} libdir=%{buildroot}/%{_libdir}

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc LICENSE*
%{_includedir}/matroska
%{_libdir}/lib*.a
%{_libdir}/lib*.so




%changelog
* Fri Sep 23 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.0-1mdv2012.0
+ Revision: 701137
- new version
- new major

* Sun Jun 26 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.0-1
+ Revision: 687344
- new version
- bump ebml dep
- new major

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 1.1.0-1
+ Revision: 634165
- New version 1.1.0
- rebuild for new ebml

* Sat Jul 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 550343
- new version
- new major
- bump ebml dep
- rename devel package

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2mdv2009.0
+ Revision: 233754
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.8.1-1mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.1-1mdv2007.0
+ Revision: 118560
- new version

* Fri Nov 03 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.0-2mdv2007.1
+ Revision: 76197
- Import libmatroska

* Wed Oct 19 2005 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdk
- bump deps
- New release 0.8.0

* Thu Jun 09 2005 Götz Waschk <waschk@mandriva.org> 0.7.7-2mdk
- mkrel

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 0.7.7-1mdk
- New release 0.7.7

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7.6-1mdk
- libify
- New release 0.7.6

* Mon Feb 07 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.7.5-1mdk
- New release 0.7.5

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-1mdk
- requires new libebml
- new version

* Tue Aug 24 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.7.3-1mdk
- New release 0.7.3

* Mon Jul 26 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.1-2mdk
- drop patch
- fix source URL
- new version

* Tue Jun 08 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.0-2mdk
- disable tests for now
- rebuild for new g++

* Sat Apr 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.0-1mdk
- requires new ebml
- new version

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6.3-2mdk
- new ebml

