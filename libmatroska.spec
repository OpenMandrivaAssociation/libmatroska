# For some reasons library is unstripped and we don't have time for investigation
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define ebmlver 1.3.0
%define major 6
%define libname %mklibname matroska %{major}
%define devname %mklibname -d matroska

Summary:	Matroska Audio/Video file format library
Name:		libmatroska
Version:	1.4.0
Release:	1
License:	GPL/QPL
Group:		System/Libraries
URL:		http://www.matroska.org/
Source0:	http://dl.matroska.org/downloads/libmatroska/%{name}-%{version}.tar.bz2
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

#----------------------------------------------------------------------------

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

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Group:		Development/C++
Summary:	Matroska Audio/Video file format headers and static library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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

%files -n %{devname}
%doc LICENSE*
%{_includedir}/matroska
%{_libdir}/lib*.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make -C make/linux CXX="g++ %{optflags} %{ldflags}"

%install
%makeinstall_std -C make/linux prefix=%{buildroot}/%{_prefix} libdir=%{buildroot}/%{_libdir}

rm -f %{buildroot}%{_libdir}/*.a


