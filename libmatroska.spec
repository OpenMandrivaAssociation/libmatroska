%define major 7
%define libname %mklibname matroska %{major}
%define devname %mklibname -d matroska

Summary:	Matroska Audio/Video file format library
Name:		libmatroska
Version:	1.7.1
Release:	2
License:	GPLv2/QPL
Group:		System/Libraries
Url:		https://www.matroska.org/
Source0:	http://dl.matroska.org/downloads/libmatroska/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libebml) >= 1.4.4
BuildRequires:  cmake

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

%package -n %{devname}
Group:		Development/C++
Summary:	Matroska Audio/Video file format headers and static library
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the C++ headers and the static library needed
for development with Matroska.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

rm -f %{buildroot}%{_libdir}/*.a

%files -n %{libname}
%{_libdir}/libmatroska.so.%{major}*

%files -n %{devname}
%doc LICENSE*
%{_includedir}/matroska
%{_libdir}/lib*.so
%{_libdir}/cmake/Matroska/Matroska*
%{_libdir}/pkgconfig/*.pc
