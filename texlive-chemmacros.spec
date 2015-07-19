# revision 33447
# category Package
# catalog-ctan /macros/latex/contrib/chemmacros
# catalog-date 2014-04-10 17:34:17 +0200
# catalog-license lppl1.3
# catalog-version 4.5
Name:		texlive-chemmacros
Version:	4.50
Release:	4
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
The bundle offers a collection of macros and commands which are
intended to make typesetting chemistry documents faster and
more convenient. Coverage includes some nomenclature commands,
oxidation numbers, thermodynamic data, newman projections, etc.
The four packages in the bundle are: chemmacros, providing the
basic requirements; chemformula (v4.2a), providing a command
for typesetting chemical formulae and reactions (doing a
similar task to that of mhchem); chemgreek (v0.2a), offering
support for use of greek letters; and ghsystem, providing for
the UN globally harmonised chemical notation. The packages are
written using current versions of the experimental LaTeX 3
coding conventions and the LaTeX 3 support packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemmacros/chemformula.sty
%{_texmfdistdir}/tex/latex/chemmacros/chemgreek.sty
%{_texmfdistdir}/tex/latex/chemmacros/chemmacros.sty
%{_texmfdistdir}/tex/latex/chemmacros/ghsystem.sty
%{_texmfdistdir}/tex/latex/chemmacros/language/ghsystem_english.def
%{_texmfdistdir}/tex/latex/chemmacros/language/ghsystem_german.def
%{_texmfdistdir}/tex/latex/chemmacros/language/ghsystem_italian.def
%{_texmfdistdir}/tex/latex/chemmacros/language/ghsystem_langtemplate.def
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_acid-8.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_acid-8.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_acid-8.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_acid-8.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_acid.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_acid.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_acid.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_acid.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_aqpol.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_aqpol.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_aqpol.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_aqpol.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle-2-black.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle-2-black.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle-2-black.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle-2-black.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle-2-white.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle-2-white.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle-2-white.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle-2-white.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_bottle.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_exclam.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_exclam.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_exclam.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_exclam.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-1.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-1.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-1.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-1.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-2.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-2.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-2.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-2.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-3.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-3.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-3.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-3.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-4.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-4.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-4.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-4.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-5.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-5.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-5.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-5.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-6.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-6.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-6.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos-6.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_explos.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-2-black.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-2-black.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-2-black.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-2-black.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-2-white.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-2-white.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-2-white.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-2-white.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-3-black.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-3-black.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-3-black.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-3-black.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-3-white.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-3-white.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-3-white.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-3-white.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-1.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-1.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-1.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-1.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-2.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-2.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-2.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-2.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-3-black.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-3-black.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-3-black.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-3-black.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-3-white.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-3-white.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-3-white.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-4-3-white.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-5-2-black.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-5-2-black.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-5-2-black.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-5-2-black.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-5-2-white.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-5-2-white.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-5-2-white.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-5-2-white.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-O-5-1.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-O-5-1.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-O-5-1.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-O-5-1.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-O.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-O.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-O.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame-O.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_flame.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_health.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_health.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_health.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_health.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull-2.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull-2.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull-2.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull-2.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull-6.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull-6.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull-6.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull-6.png
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull.eps
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull.jpg
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull.pdf
%{_texmfdistdir}/tex/latex/chemmacros/pictures/ghsystem_skull.png
%doc %{_texmfdistdir}/doc/latex/chemmacros/README
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemformula_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemformula_en.tex
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemformula_test_sub_and_superscripts.tex
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemgreek_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemgreek_en.tex
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_en.tex
%doc %{_texmfdistdir}/doc/latex/chemmacros/ghsystem_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemmacros/ghsystem_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
