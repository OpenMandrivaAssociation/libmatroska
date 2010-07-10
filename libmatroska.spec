%define name    libmatroska
%define version 1.0.0
%define ebmlver 1.0.0
%define major 2
%define libname %mklibname matroska %major
%define develname %mklibname -d matroska

Summary:        Matroska Audio/Video file format library
Name:           %name
Version:        %version
Release:	%mkrel 1
License:        GPL/QPL
Group:		System/Libraries
URL:            http://www.matroska.org/
Source0:        http://dl.matroska.org/downloads/libmatroska/%name-%version.tar.bz2
BuildRequires:  libebml-devel >= %ebmlver
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n %libname
Summary:        Matroska Audio/Video file format shared library
Group: System/Libraries

%description -n %libname
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

%package -n %develname
Group: Development/C++
Summary: Matroska Audio/Video file format headers and static library
Requires: %libname = %version
Provides: libmatroska-devel = %version-%release
Obsoletes: %mklibname -d matroska 0

%description -n %develname
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
%make


%install
rm -rf %buildroot
cd make/linux
%makeinstall_std prefix=%buildroot/%_prefix libdir=%buildroot/%_libdir

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc LICENSE*
%{_includedir}/matroska
%{_libdir}/lib*.a
%{_libdir}/lib*.so


