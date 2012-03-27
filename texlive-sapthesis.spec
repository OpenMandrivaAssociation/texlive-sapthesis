# revision 25593
# category Package
# catalog-ctan /macros/latex/contrib/sapthesis
# catalog-date 2012-03-09 11:37:27 +0100
# catalog-license lppl1.3
# catalog-version 3.1.1
Name:		texlive-sapthesis
Version:	3.1.1
Release:	1
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
%{_texmfdistdir}/tex/latex/sapthesis/sapienza-MLblack-pos.pdf
%{_texmfdistdir}/tex/latex/sapthesis/sapienza-MLred-pos.pdf
%{_texmfdistdir}/tex/latex/sapthesis/sapthesis.cls
%doc %{_texmfdistdir}/doc/latex/sapthesis/README
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
