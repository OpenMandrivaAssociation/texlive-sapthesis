# revision 31487
# category Package
# catalog-ctan /macros/latex/contrib/sapthesis
# catalog-date 2013-08-21 10:23:24 +0200
# catalog-license lppl1.3
# catalog-version 3.2
Name:		texlive-sapthesis
Version:	3.2
Release:	7
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
%doc %{_texmfdistdir}/doc/latex/sapthesis/examples/Laurea.tex
%doc %{_texmfdistdir}/doc/latex/sapthesis/examples/LaureaMagistrale.tex
%doc %{_texmfdistdir}/doc/latex/sapthesis/examples/Master.tex
%doc %{_texmfdistdir}/doc/latex/sapthesis/examples/PhD.tex
%doc %{_texmfdistdir}/doc/latex/sapthesis/examples/Specialization.tex
%doc %{_texmfdistdir}/doc/latex/sapthesis/examples/TFA.tex
%doc %{_texmfdistdir}/doc/latex/sapthesis/sapthesis-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sapthesis/sapthesis-doc.tex
%doc %{_texmfdistdir}/doc/latex/sapthesis/sapthesis.layout

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
