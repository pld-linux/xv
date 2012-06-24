Summary:	X based image viewer for darned near all images
Summary(de.UTF-8):   X-basierender Bild-Viewer für praktische sämtliche Grafiken
Summary(es.UTF-8):   Visualizador de imágenes para X para cuasi todos los formatos de imágenes
Summary(fr.UTF-8):   Visualisateur sous X pour quasiment tous les types d'images
Summary(pl.UTF-8):   Przeglądarka różnego rodzaju plików graficznych pracująca w X Window
Summary(pt_BR.UTF-8):   Visualizador de imagens para X para quase todos os formatos de imagens
Summary(ru.UTF-8):   Программа для просмотра и преобразования файлов изображений для X
Summary(tr.UTF-8):   X tabanlı resim görüntüleyici
Summary(uk.UTF-8):   Програма для перегляду та перетворення файлів зображень для X
Name:		xv
Version:	3.10a
Release:	28
License:	Shareware
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.cis.upenn.edu/pub/xv/%{name}-%{version}.tar.gz
# Source0-md5:	2d4fbeec1561304362781cc8e2f7f72d
Source1:	ftp://swrinde.nde.swri.edu/pub/png/applications/%{name}-%{version}-png-1.2d.tar.gz
# Source1-md5:	c8cbe14db6e2104ed4eb5330cdaba420
Source2:	%{name}man310a-html.tar.gz
# Source2-md5:	78dce344e3e85faf01e1f13014aa659b
Source3:	%{name}.desktop
Source4:	%{name}.png
Source5:	%{name}-non-english-Xman-pages.tar.bz2
# Source5-md5:	4e5a6582ad76974309ca8bf8fb56b671
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
Patch14:	%{name}-c.patch
URL:		http://www.trilon.com/xv/xv.html
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	sed
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the famous 'xv' by John Bradley. It is shareware, but we ship
it with the permission of the authors. It is a graphics viewer for
many file types, including gif, jpg, tiff, xwd, etc. It also has
manipulation features such as cropping, expanding, etc. Patched to
include flmask, a popular feature in Japan.

%description -l de.UTF-8
Dies ist das berühmte 'xv' von John Bradley, ein Shareware- Programm,
das wir mit Erlaubnis des Autors liefern. Es ist ein Grafik-Viewer für
diverse Dateitypen, einschließlich gif, funktionen wie Trimmen,
Strecken u.ä. Mit flmask.

%description -l es.UTF-8
Este es el famoso 'xv' de John Bradley. Es shareware, pero nosotros lo
distribuimos con la permisión de los autores. Es un visor gráfico para
varios tipos de archivos, incluyendo gif, jpg, tiff, xwd, etc. También
posee características de manejo como corte, expansión, etc.

%description -l fr.UTF-8
Le célébre xv de John Bradley. C'est shareware, mais nous le
distribuons avec la permission de l'auteur. C'est un visualiseur
graphique pour de nombreux formats de fichier dont gif, jpg, tiff,
xwd, etc. Il offre aussi des fonctionnalités comme la capture,
l'extension, la retouche de palette, etc. Flmask.

%description -l pl.UTF-8
Słynne 'xv' Johna Bradleya. Jest to program shareware, ale
udostępniamy go za zgodą autora. Jest to przeglądarka plików
graficznych w różnych formatach, takich jak: gif, jpg, tiff, xwd i
innych. Ma też proste możliwości obróbki obrazków, takie jak obcinanie
czy rozszerzanie. Zawiera obsługę flmask.

%description -l pt_BR.UTF-8
Este é o famoso 'xv' de John Bradley. Ele é shareware, mas nós o
distribuimos com a permissão dos autores. É um visualizador gráfico
para vários tipos de arquivos, incluindo gif, jpg, tiff, xwd, etc.
Também possui características de manipulação como corte, expansão,
etc.

%description -l ru.UTF-8
Xv - это программа для просмотра и преобразования изображений для X
Window System. Xv умеет показывать GIF, JPEG, TIFF, PBM, PPM, PDF, X11
bitmap, Utah Raster Toolkit RLE, PDS/VICAR, Sun Rasterfile, BMP, PCX,
IRIS RGB, XPM, Targa, XWD, PostScript(TM) и PM. Xv также умеет делать
простую обработку изображений - cropping, expanding, снимки экрана и
т.п.

%description -l tr.UTF-8
xv başta PNG, GIF, JPG, BMP, XBM, XPM olmak üzere birçok resim
dosyasını görüntüleyebilir, değişik formatlarda kaydedebilir ve
üzerinde boyutlandırma, renk değiştirme gibi bazı temel işlemleri
yapabilir. Çok detaylı işlemler yapamamasına rağmen temel resim
işlemlerinde öncellikle kullanılabilecek, kullanışlı arayüzüne sahip
bir programdır. Flmask.

%description -l uk.UTF-8
Xv - це програма для перегляду та перетворення зображень для X Window
System. Xv вміє показувати GIF, JPEG, TIFF, PBM, PPM, PDF, X11 bitmap,
Utah Raster Toolkit RLE, PDS/VICAR, Sun Rasterfile, BMP, PCX, IRIS
RGB, XPM, Targa, XWD, PostScript(TM) та PM. Xv також вміє робити
просту обробку зображень - cropping, expanding, знімки экрану і т.і.

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
%patch14 -p1
tar zxf %{SOURCE2}

%build
%{__make} \
	CC="%{__cc}" \
	CCOPTS="%{rpmcflags} `pkg-config --cflags libpng12 2>/dev/null`" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
mv -f xvman310a manual

bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/xvdocs.ps BUGS CHANGELOG IDEAS CPMASK 00_README manual
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/xv.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(pl) %{_mandir}/pl/man1/*
