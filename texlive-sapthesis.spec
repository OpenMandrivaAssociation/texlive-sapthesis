Name:		texlive-sapthesis
Version:	63810
Release:	1
Summary:	Typeset theses for Sapienza-University, Rome
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sapthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sapthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sapthesis.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/sapthesis
%{_texmfdistdir}/tex/latex/sapthesis
%doc %{_texmfdistdir}/doc/latex/sapthesis

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
