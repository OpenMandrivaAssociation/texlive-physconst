Name:		texlive-physconst
Version:	58727
Release:	1
Summary:	Macros for commonly used physical constants
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/physconst
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physconst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physconst.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physconst.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package consists of several macros that are shorthand for
a variety of physical constants, e.g. the speed of light. The
package developed out of physics and astronomy classes that the
author has taught and wanted to ensure that he had correct
values for each constant and did not wish to retype them every
time he uses them. The constants can be used in two forms, the
most accurate available values, or versions that are rounded to
3 significant digits for use in typical classroom settings,
homework assignments, etc. Most constants are taken from CODATA
2018, with the exception of the astronomical objects, whose
values are taken from International Astronomical Union
specified values. Constants that are derived from true
constants, e.g. the fine structure constant, have been
calculated using the accepted values of the fundamental
constants.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/physconst
%{_texmfdistdir}/tex/latex/physconst
%doc %{_texmfdistdir}/doc/latex/physconst

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
