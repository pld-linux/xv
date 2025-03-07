Summary:	X based image viewer for darned near all images
Summary(de.UTF-8):	X-basierender Bild-Viewer für praktische sämtliche Grafiken
Summary(es.UTF-8):	Visualizador de imágenes para X para cuasi todos los formatos de imágenes
Summary(fr.UTF-8):	Visualisateur sous X pour quasiment tous les types d'images
Summary(pl.UTF-8):	Przeglądarka różnego rodzaju plików graficznych pracująca w X Window
Summary(pt_BR.UTF-8):	Visualizador de imagens para X para quase todos os formatos de imagens
Summary(ru.UTF-8):	Программа для просмотра и преобразования файлов изображений для X
Summary(tr.UTF-8):	X tabanlı resim görüntüleyici
Summary(uk.UTF-8):	Програма для перегляду та перетворення файлів зображень для X
Name:		xv
Version:	6.0.3
Release:	1
License:	Shareware
Group:		X11/Applications/Graphics
Source0:	https://github.com/jasper-software/xv/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	8c5dea54cada4833dbe4a47d99d07e3f
URL:		http://www.trilon.com/xv/xv.html
BuildRequires:	cmake
BuildRequires:	jasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.2
BuildRequires:	libtiff-devel
BuildRequires:	libwebp-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
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

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database

%prep
%setup -q

%build
mkdir build_dir
cd build_dir
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build_dir
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt NEWS.txt README.md src/{README,README.FLmask,README.debian,README.jumbo,README.pcd,README.xv-non-english-Xman-pages,docs}
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/xv_mgcsfx
%{_desktopdir}/xv.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(pl) %{_mandir}/pl/man1/*
