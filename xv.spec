Summary:	X based image viewer for darned near all images
Summary(de):	X-basierender Bild-Viewer für praktische sämtliche Grafiken
Summary(fr):	Visualisateur sous X pour quasiment tous les types d'images
Summary(tr):	X tabanlý resim görüntüleyici
Name:		xv
Version:	3.10a
Release:	1
Copyright:	Shareware
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.cis.upenn.edu/pub/xv/%{name}-%{version}.tar.gz
Source1:	ftp://swrinde.nde.swri.edu/pub/png/applications/xv-3.10a-png-1.2d.tar.gz
Source2:	xvman310a-html.tar.gz
Source3:	xv.desktop
Patch0:		xv-PLD.patch
Patch1:		xv-3.10a-FLmask.v2.1.patch
Patch2:		xv-3.10a.JPEG-patch
Patch3:		xv-3.10a.TIFF-patch
Patch4:		xv-croppad.patch
Patch5:		xv-deepcolor.patch
Patch6:		xv-exceed_grab_patch.txt
Patch7:		xv-gifpatch
Patch8:		xv-grabpatch
Patch9:		xv-longname.patch
Patch10:	xv-mp-tiff-patch
Patch11:	xv-pdf.patch
Patch12:	xv-png-fix2.patch
Patch13:	xv-vispatch
URL:		http://www.trilon.com/xv/xv.html
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
This is the famous 'xv' by John Bradley.  It is shareware, but
we ship it with the permission of the authors.  It is a graphics
viewer for many file types, including gif, jpg, tiff, xwd, etc.
It also has manipulation features such as cropping, expanding, etc.
Patched to include flmask, a popular feature in Japan.

%description -l de
Dies ist das berühmte 'xv' von John Bradley, ein Shareware-
Programm, das wir mit Erlaubnis des Autors liefern. Es ist
ein Grafik-Viewer für diverse Dateitypen, einschließlich gif, 
funktionen wie Trimmen, Strecken u.ä.  Mit flmask.

%description -l fr
Le célébre xv de John Bradley. C'est shareware, mais nous le distribuons
avec la permission de l'auteur. C'est un visualiseur graphique pour
de nombreux formats de fichier dont gif, jpg, tiff, xwd, etc.
Il offre aussi des fonctionnalités comme la capture, l'extension,
la retouche de palette, etc.  Flmask.

%description -l tr
xv baþta PNG, GIF, JPG, BMP, XBM, XPM olmak üzere birçok resim dosyasýný
görüntüleyebilir, deðiþik formatlarda kaydedebilir ve üzerinde boyutlandýrma,
renk deðiþtirme gibi bazý temel iþlemleri yapabilir. Çok detaylý iþlemler
yapamamasýna raðmen temel resim iþlemlerinde öncellikle kullanýlabilecek,
kullanýþlý arayüzüne sahip bir programdýr.  Flmask.

%prep
%setup -q
tar xvfz %{SOURCE1}
patch -p1 --quiet < xvpng.diff
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p1
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
tar zxf %{SOURCE2}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}
install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/Viewers
install -d $RPM_BUILD_ROOT/home/httpd/html/%{name}-%{version}

make install\
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/Viewers
cp -a xvman310a/* $RPM_BUILD_ROOT/home/httpd/html/%{name}-%{version}/

gzip -9nf README docs/xvdocs.ps BUGS CHANGELOG IDEAS CPMASK 00_README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,docs/xvdocs.ps,BUGS,CHANGELOG,IDEAS,CPMASK,00_README}.gz
%docdir /home/httpd/html/%{name}-%{version}
%doc /home/httpd/html/%{name}-%{version}/*
%{_datadir}/applnk/Graphics/Viewers/xv.desktop
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
