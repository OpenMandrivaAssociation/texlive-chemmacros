%global tl_name chemmacros
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.2a
Release:	%{tl_revision}.1
Summary:	A collection of macros to support typesetting chemistry documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemmacros
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemmacros.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemmacros.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle offers a collection of macros and commands which are intended
to make typesetting chemistry documents faster and more convenient.
Coverage includes some nomenclature commands, oxidation numbers,
thermodynamic data, newman projections, etc. The package relies on the
following supporting packages: chemformula, providing a command for
typesetting chemical formulae and reactions (doing a similar task to
that of mhchem); chemgreek, offering support for use of greek letters;
and ghsystem, providing for the UN globally harmonised chemical
notation. The packages are written using current versions of the
experimental LaTeX 3 coding conventions and the LaTeX 3 support
packages.

