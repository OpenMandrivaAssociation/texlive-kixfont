# revision 18488
# category Package
# catalog-ctan /fonts/kixfont
# catalog-date 2007-10-05 20:57:01 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-kixfont
Version:	20071005
Release:	1
Summary:	A font for KIX codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/kixfont
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kixfont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kixfont.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The KIX code is a barcode-like format used by the Dutch PTT to
encode country codes, zip codes and street numbers in a
machine-readable format. If printed below the address line on
bulk mailings, a discount can be obtained. The font is
distributed in MetaFont format, and covers the numbers and
upper-case letters.

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
%{_texmfdistdir}/fonts/source/public/kixfont/kix.mf
%{_texmfdistdir}/fonts/tfm/public/kixfont/kix.tfm
%doc %{_texmfdistdir}/doc/fonts/kixfont/kix.mf.asc
%doc %{_texmfdistdir}/doc/fonts/kixfont/kixtable.pdf
%doc %{_texmfdistdir}/doc/fonts/kixfont/kixtable.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
