%global tl_name physconst
%global tl_revision 58727

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Macros for commonly used physical constants
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/physconst
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/physconst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/physconst.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/physconst.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package consists of several macros that are shorthand for a variety
of physical constants, e.g. the speed of light. The package developed
out of physics and astronomy classes that the author has taught and
wanted to ensure that he had correct values for each constant and did
not wish to retype them every time he uses them. The constants can be
used in two forms, the most accurate available values, or versions that
are rounded to 3 significant digits for use in typical classroom
settings, homework assignments, etc. Most constants are taken from
CODATA 2018, with the exception of the astronomical objects, whose
values are taken from International Astronomical Union specified values.
Constants that are derived from true constants, e.g. the fine structure
constant, have been calculated using the accepted values of the
fundamental constants.

