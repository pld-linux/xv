Summary:	X based image viewer for darned near all images
Summary(pl):	Przegl�darka r�nego rodzaju plik�w graficznych pracuj�ca w X Window
Summary(de):	X-basierender Bild-Viewer f�r praktische s�mtliche Grafiken
Summary(fr):	Visualisateur sous X pour quasiment tous les types d'images
Summary(tr):	X tabanl� resim g�r�nt�leyici
Name:		xv
Version:	3.10a
Release:	19
Copyright:	Shareware
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.cis.upenn.edu/pub/xv/%{name}-%{version}.tar.gz
Source1:	ftp://swrinde.nde.swri.edu/pub/png/applications/%{name}-%{version}-png-1.2d.tar.gz
Source2:	%{name}man310a-html.tar.gz
Source3:	%{name}.desktop
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-FLmask.v2.1.patch
Patch2:		%{name}-JPEG.patch
Patch3:		%{name}-TIFF.patch
Patch4:		%{name}-croppad.patch
Patch5:		%{name}-deepcolor.patch
Patch6:		%{name}-exceed_grab_patch.txt
Patch7:		%{name}-gifpatch
Patch8:		%{name}-grabpatch
Patch9:		%{name}-longname.patch
Patch10:	%{name}-mp-tiff-patch
Patch11:	%{name}-pdf.patch
Patch12:	%{name}-png-fix2.patch
Patch13:	%{name}-vispatch
URL:		http://www.trilon.com/xv/xv.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is the famous 'xv' by John Bradley. It is shareware, but we ship
it with the permission of the authors. It is a graphics viewer for
many file types, including gif, jpg, tiff, xwd, etc. It also has
manipulation features such as cropping, expanding, etc. Patched to
include flmask, a popular feature in Japan.

%description -l pl
S�ynne 'xv' Johna Bradley'a. Jest to program shareware, ale
udost�pniamy go za zgod� autora. Jest to przegl�darka plik�w
graficznych w r�nych formatach, takich jak: gif, jpg, tiff, xwd i
innych. Daje tak�e mo�liwo�� prostego mainupulowania obrazkiem.
Zawiera obs�ug� flmask.

%description -l de
Dies ist das ber�hmte 'xv' von John Bradley, ein Shareware- Programm,
das wir mit Erlaubnis des Autors liefern. Es ist ein Grafik-Viewer f�r
diverse Dateitypen, einschlie�lich gif, funktionen wie Trimmen,
Strecken u.�. Mit flmask.

%description -l fr
Le c�l�bre xv de John Bradley. C'est shareware, mais nous le
distribuons avec la permission de l'auteur. C'est un visualiseur
graphique pour de nombreux formats de fichier dont gif, jpg, tiff,
xwd, etc. Il offre aussi des fonctionnalit�s comme la capture,
l'extension, la retouche de palette, etc. Flmask.

%description -l tr
xv ba�ta PNG, GIF, JPG, BMP, XBM, XPM olmak �zere bir�ok resim
dosyas�n� g�r�nt�leyebilir, de�i�ik formatlarda kaydedebilir ve
�zerinde boyutland�rma, renk de�i�tirme gibi baz� temel i�lemleri
yapabilir. �ok detayl� i�lemler yapamamas�na ra�men temel resim
i�lemlerinde �ncellikle kullan�labilecek, kullan��l� aray�z�ne sahip
bir programd�r. Flmask.

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
%{__make} CCOPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers \
	$RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}
 
%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
mv -f xvman310a manual

gzip -9nf README docs/xvdocs.ps BUGS CHANGELOG IDEAS CPMASK 00_README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,docs/xvdocs.ps,BUGS,CHANGELOG,IDEAS,CPMASK,00_README}.gz
%doc manual
%{_applnkdir}/Graphics/Viewers/xv.desktop
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
