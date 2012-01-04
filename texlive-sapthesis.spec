# revision 23939
# category Package
# catalog-ctan /macros/latex/contrib/sapthesis
# catalog-date 2011-09-13 13:48:05 +0200
# catalog-license lppl1.3
# catalog-version 2.8
Name:		texlive-sapthesis
Version:	2.8
Release:	2
Summary:	Typeset theses for Sapienza-University, Rome
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sapthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sapthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sapthesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class will typeset Ph.D., Master, and Bachelor theses that
adhere to the publishing guidelines of the Sapienza-University
of Rome.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/sapthesis/sapthesis.bst
%{_texmfdistdir}/tex/latex/sapthesis/sapthesis.cls
%doc %{_texmfdistdir}/doc/latex/sapthesis/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/sapthesis/README.sapthesis
%doc %{_texmfdistdir}/doc/latex/sapthesis/sapthesis-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sapthesis/sapthesis-doc.tex
%doc %{_texmfdistdir}/doc/latex/sapthesis/sapthesis-example.pdf
%doc %{_texmfdistdir}/doc/latex/sapthesis/sapthesis-example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
