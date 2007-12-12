%define	name		rawphoto
%define	version		1.19
%define	subversion	%nil
#define	release		0.%{subversion}.1mdk
%define releasedate	200410220910
%define	release		%mkrel 3

Name:		%name
Version:	%version
Release:	%release
Summary:	Reads the raw image formats of digital cameras into GIMP
Group:		Graphics
# Disappeared upstream
#URL:		http://ptj.rozeta.com.pl/Soft/RawPhoto
Source0:	http://ptj.rozeta.com.pl/Soft/rawphoto/%{name}-%{releasedate}.tar.bz2
License:	GPL
Requires:	dcraw gimp
Conflicts:	dcraw-gimp2.0 ufraw
#BuildRequires:	liblcms-devel libart_lgpl2-devel libgdk-pixbuf2-devel 
BuildRequires:	libgimp-devel >= 2.0 libgtk+-devel
Buildroot:	%_tmppath/%name-%version-%release-root

%description

A GIMP plug-in which reads and processes raw images from most digital
cameras. The conversion is done by the dcraw software and so all
cameras supported by dcraw are also supported by this plug-in.

Raw images are the data directly read from the CCD of the camera,
without in-camera processing, without lossy JPEG compression, and in
36 or 48 bits color depth (TIFF has 24 bits). Problem of the raw
images is that they are in proprietary, camera-specific formats as
they are exactly what the CCD has captured, and the CCDs on differnt
cameras are very different. It also contains info about the camera
settings.

In contrary to the original GIMP plug-in of dcraw this one is much
more comfortable, especially because of the life preview image but
also due to more options.

The upstream home page of this package disappeared, so the package is
most probably not maintained any more. Enjoy it as long as it works,
but as soon as it stops building or working, we will remove it from
the distribution.

%prep
rm -rf $RPM_BUILD_DIR/%{name}-%{releasedate}

%setup -q -n %{name}-%{releasedate}

%build
cd $RPM_BUILD_DIR/%{name}-%{releasedate}

#configure --with-lcms-includes=/usr/include/lcms
#configure

#perl -p -i -e 's:-L/usr/lib:-L/usr/lib -L/usr/X11R6/lib/:' src/Makefile
perl -p -i -e 's:gimptool:gimptool-2.0:' Makefile */Makefile
make

%install
cd $RPM_BUILD_DIR/%{name}-%{releasedate}

install -d %{buildroot}%{_libdir}/gimp/2.0/plug-ins
install -m 755 src/rawphoto %{buildroot}%{_libdir}/gimp/2.0/plug-ins
#makeinstall
%find_lang rawphoto

%clean
rm -fr %buildroot

%files -f rawphoto.lang
%defattr(-,root,root)
%docdir %{_docdir}/%{name}-%{version}%{subversion}
%doc README
%{_libdir}/gimp/2.0/plug-ins/*

