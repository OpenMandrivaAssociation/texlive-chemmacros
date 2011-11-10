# revision 24494
# category Package
# catalog-ctan /macros/latex/contrib/chemmacros
# catalog-date 2011-11-03 22:55:24 +0100
# catalog-license lppl1.3
# catalog-version 2.0a
Name:		texlive-chemmacros
Version:	2.0a
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package offers a collection of macros and commands which
are intended to make typesetting chemistry documents faster and
more convenient. Coverage includes some nomenclature commands,
oxidation numbers, thermodynamic data, newman projections, etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemmacros/chemmacros-version1.cfg
%{_texmfdistdir}/tex/latex/chemmacros/chemmacros.sty
%doc %{_texmfdistdir}/doc/latex/chemmacros/README
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_doc_de.pdf
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_doc_de.tex
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_doc_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemmacros/chemmacros_doc_en.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
