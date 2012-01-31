# revision 25241
# category Package
# catalog-ctan /macros/latex/contrib/chemmacros
# catalog-date 2012-01-30 22:51:08 +0100
# catalog-license lppl1.3
# catalog-version 3.0a
Name:		texlive-chemmacros
Version:	3.0a
Release:	1
Summary:	A collection of macros to support typesetting chemistry documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemmacros
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemmacros.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemmacros.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a collection of macros and commands which
are intended to make typesetting chemistry documents faster and
more convenient. Coverage includes some nomenclature commands,
oxidation numbers, thermodynamic data, newman projections, etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemmacros/chemformula.sty
%{_texmfdistdir}/tex/latex/chemmacros/chemmacros-version1.cfg
%{_texmfdistdir}/tex/latex/chemmacros/chemmacros.sty
%{_texmfdistdir}/tex/latex/chemmacros/ghsystem.sty
%doc %{_texmfdistdir}/doc/latex/chemmacros/README
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros-codehelper.tex
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_doc_de.pdf
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_doc_de.tex
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_doc_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_doc_en.tex
%doc %{_texmfdistdir}/doc/latex/chemmacros/language/ghsystem_english.def
%doc %{_texmfdistdir}/doc/latex/chemmacros/language/ghsystem_german.def
%doc %{_texmfdistdir}/doc/latex/chemmacros/language/ghsystem_langtemplate.def
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/acid-8.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/acid-8.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/acid-8.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/acid.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/acid.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/acid.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/aqpol.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/aqpol.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/aqpol.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle-2-black.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle-2-black.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle-2-black.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle-2-white.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle-2-white.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle-2-white.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/bottle.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/exclam.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/exclam.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/exclam.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-1.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-1.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-1.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-2.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-2.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-2.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-3.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-3.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-3.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-4.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-4.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-4.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-5.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-5.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-5.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-6.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-6.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos-6.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/explos.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-2-black.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-2-black.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-2-black.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-2-white.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-2-white.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-2-white.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-3-black.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-3-black.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-3-black.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-3-white.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-3-white.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-3-white.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-1.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-1.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-1.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-2.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-2.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-2.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-3-black.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-3-black.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-3-black.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-3-white.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-3-white.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-4-3-white.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-5-2-black.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-5-2-black.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-5-2-black.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-5-2-white.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-5-2-white.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-5-2-white.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-O-5-1.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-O-5-1.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-O-5-1.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-O.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-O.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame-O.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/flame.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/health.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/health.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/health.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull-2.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull-2.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull-2.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull-6.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull-6.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull-6.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull.eps
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull.jpg
%doc %{_texmfdistdir}/doc/latex/chemmacros/pictures/skull.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
