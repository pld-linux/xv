Summary:	X based image viewer for darned near all images
Summary(de):	X-basierender Bild-Viewer für praktische sämtliche Grafiken
Summary(es):	Visualizador de imágenes para X para cuasi todos los formatos de imágenes
Summary(fr):	Visualisateur sous X pour quasiment tous les types d'images
Summary(pl):	Przegl±darka ró¿nego rodzaju plików graficznych pracuj±ca w X Window
Summary(pt_BR):	Visualizador de imagens para X para quase todos os formatos de imagens
Summary(tr):	X tabanlý resim görüntüleyici
Name:		xv
Version:	3.10a
Release:	20
Copyright:	Shareware
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Group(pt):	X11/Aplicações/Gráficos
Source0:	ftp://ftp.cis.upenn.edu/pub/xv/%{name}-%{version}.tar.gz
Source1:	ftp://swrinde.nde.swri.edu/pub/png/applications/%{name}-%{version}-png-1.2d.tar.gz
Source2:	%{name}man310a-html.tar.gz
Source3:	%{name}.desktop
Source4:	%{name}-non-english-Xman-pages.tar.bz2
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

%description -l de
Dies ist das berühmte 'xv' von John Bradley, ein Shareware- Programm,
das wir mit Erlaubnis des Autors liefern. Es ist ein Grafik-Viewer für
diverse Dateitypen, einschließlich gif, funktionen wie Trimmen,
Strecken u.ä. Mit flmask.

%description -l es
Este es el famoso 'xv' de John Bradley. Es shareware, pero nosotros lo
distribuimos con la permisión de los autores. Es un visor gráfico para
varios tipos de archivos, incluyendo gif, jpg, tiff, xwd, etc. También
posee características de manejo como corte, expansión, etc.

%description -l fr
Le célébre xv de John Bradley. C'est shareware, mais nous le
distribuons avec la permission de l'auteur. C'est un visualiseur
graphique pour de nombreux formats de fichier dont gif, jpg, tiff,
xwd, etc. Il offre aussi des fonctionnalités comme la capture,
l'extension, la retouche de palette, etc. Flmask.

%description -l pl
S³ynne 'xv' Johna Bradley'a. Jest to program shareware, ale
udostêpniamy go za zgod± autora. Jest to przegl±darka plików
graficznych w ró¿nych formatach, takich jak: gif, jpg, tiff, xwd i
innych. Daje tak¿e mo¿liwo¶æ prostego mainupulowania obrazkiem.
Zawiera obs³ugê flmask.

%description -l tr
xv baþta PNG, GIF, JPG, BMP, XBM, XPM olmak üzere birçok resim
dosyasýný görüntüleyebilir, deðiþik formatlarda kaydedebilir ve
üzerinde boyutlandýrma, renk deðiþtirme gibi bazý temel iþlemleri
yapabilir. Çok detaylý iþlemler yapamamasýna raðmen temel resim
iþlemlerinde öncellikle kullanýlabilecek, kullanýþlý arayüzüne sahip
bir programdýr. Flmask.

%description -l pt_BR
Este é o famoso 'xv' de John Bradley. Ele é shareware, mas nós o
distribuimos com a permissão dos autores. É um visualizador gráfico
para vários tipos de arquivos, incluindo gif, jpg, tiff, xwd, etc.
Também possui características de manipulação como corte, expansão,
etc.

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

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

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
%lang(fi) %{_mandir}/fi/man1/*
%lang(pl) %{_mandir}/pl/man1/*
