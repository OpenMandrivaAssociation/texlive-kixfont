%global tl_name kixfont
%global tl_revision 18488

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A font for KIX codes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/kixfont
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kixfont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kixfont.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The KIX code is a barcode-like format used by the Dutch PTT to encode
country codes, zip codes and street numbers in a machine-readable
format. If printed below the address line on bulk mailings, a discount
can be obtained. The font is distributed in Metafont format, and covers
the numbers and upper-case letters.

