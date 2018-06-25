Name:		texlive-kixfont
Version:	20180303
Release:	1
Summary:	A font for KIX codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/kixfont
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kixfont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kixfont.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The KIX code is a barcode-like format used by the Dutch PTT to
encode country codes, zip codes and street numbers in a
machine-readable format. If printed below the address line on
bulk mailings, a discount can be obtained. The font is
distributed in MetaFont format, and covers the numbers and
upper-case letters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/kixfont
%{_texmfdistdir}/fonts/tfm/public/kixfont
%doc %{_texmfdistdir}/doc/fonts/kixfont

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
