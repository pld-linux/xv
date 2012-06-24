Summary:	X based image viewer for darned near all images
Summary(de):	X-basierender Bild-Viewer f�r praktische s�mtliche Grafiken
Summary(es):	Visualizador de im�genes para X para cuasi todos los formatos de im�genes
Summary(fr):	Visualisateur sous X pour quasiment tous les types d'images
Summary(pl):	Przegl�darka r�nego rodzaju plik�w graficznych pracuj�ca w X Window
Summary(pt_BR):	Visualizador de imagens para X para quase todos os formatos de imagens
Summary(ru):	��������� ��� ��������� � �������������� ������ ����������� ��� X
Summary(tr):	X tabanl� resim g�r�nt�leyici
Summary(uk):	�������� ��� ��������� �� ������������ ���̦� ��������� ��� X
Name:		xv
Version:	3.10a
Release:	24
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
URL:		http://www.trilon.com/xv/xv.html
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is the famous 'xv' by John Bradley. It is shareware, but we ship
it with the permission of the authors. It is a graphics viewer for
many file types, including gif, jpg, tiff, xwd, etc. It also has
manipulation features such as cropping, expanding, etc. Patched to
include flmask, a popular feature in Japan.

%description -l de
Dies ist das ber�hmte 'xv' von John Bradley, ein Shareware- Programm,
das wir mit Erlaubnis des Autors liefern. Es ist ein Grafik-Viewer f�r
diverse Dateitypen, einschlie�lich gif, funktionen wie Trimmen,
Strecken u.�. Mit flmask.

%description -l es
Este es el famoso 'xv' de John Bradley. Es shareware, pero nosotros lo
distribuimos con la permisi�n de los autores. Es un visor gr�fico para
varios tipos de archivos, incluyendo gif, jpg, tiff, xwd, etc. Tambi�n
posee caracter�sticas de manejo como corte, expansi�n, etc.

%description -l fr
Le c�l�bre xv de John Bradley. C'est shareware, mais nous le
distribuons avec la permission de l'auteur. C'est un visualiseur
graphique pour de nombreux formats de fichier dont gif, jpg, tiff,
xwd, etc. Il offre aussi des fonctionnalit�s comme la capture,
l'extension, la retouche de palette, etc. Flmask.

%description -l pl
S�ynne 'xv' Johna Bradley'a. Jest to program shareware, ale
udost�pniamy go za zgod� autora. Jest to przegl�darka plik�w
graficznych w r�nych formatach, takich jak: gif, jpg, tiff, xwd i
innych. Daje tak�e mo�liwo�� prostego mainupulowania obrazkiem.
Zawiera obs�ug� flmask.

%description -l pt_BR
Este � o famoso 'xv' de John Bradley. Ele � shareware, mas n�s o
distribuimos com a permiss�o dos autores. � um visualizador gr�fico
para v�rios tipos de arquivos, incluindo gif, jpg, tiff, xwd, etc.
Tamb�m possui caracter�sticas de manipula��o como corte, expans�o,
etc.

%description -l ru
Xv - ��� ��������� ��� ��������� � �������������� ����������� ��� X
Window System. Xv ����� ���������� GIF, JPEG, TIFF, PBM, PPM, PDF, X11
bitmap, Utah Raster Toolkit RLE, PDS/VICAR, Sun Rasterfile, BMP, PCX,
IRIS RGB, XPM, Targa, XWD, PostScript(TM) � PM. Xv ����� ����� ������
������� ��������� ����������� - cropping, expanding, ������ ������ �
�.�.

%description -l tr
xv ba�ta PNG, GIF, JPG, BMP, XBM, XPM olmak �zere bir�ok resim
dosyas�n� g�r�nt�leyebilir, de�i�ik formatlarda kaydedebilir ve
�zerinde boyutland�rma, renk de�i�tirme gibi baz� temel i�lemleri
yapabilir. �ok detayl� i�lemler yapamamas�na ra�men temel resim
i�lemlerinde �ncellikle kullan�labilecek, kullan��l� aray�z�ne sahip
bir programd�r. Flmask.

%description -l uk
Xv - �� �������� ��� ��������� �� ������������ ��������� ��� X Window
System. Xv �ͦ� ���������� GIF, JPEG, TIFF, PBM, PPM, PDF, X11 bitmap,
Utah Raster Toolkit RLE, PDS/VICAR, Sun Rasterfile, BMP, PCX, IRIS
RGB, XPM, Targa, XWD, PostScript(TM) �� PM. Xv ����� �ͦ� ������
������ ������� ��������� - cropping, expanding, �Φ��� ������ � �.�.

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
%{__make} CCOPTS="%{rpmcflags} `pkg-config --cflags libpng12 2>/dev/null`"

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
