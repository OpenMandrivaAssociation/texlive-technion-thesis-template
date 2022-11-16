Name:		texlive-technion-thesis-template
Version:	49889
Release:	1
Summary:	Template for theses on the Technion graduate school
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/technion-thesis-template
License:	cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/technion-thesis-template.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/technion-thesis-template.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a template for writing a thesis according to the
Technion specifications.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/technion-thesis-template
%doc %{_texmfdistdir}/doc/xelatex/technion-thesis-template

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
