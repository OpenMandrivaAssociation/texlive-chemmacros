Name:		texlive-chemmacros
Version:	5.8b
Release:	2
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
%{_texmfdistdir}/tex/latex/chemmacros
%doc %{_texmfdistdir}/doc/latex/chemmacros

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
