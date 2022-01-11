#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Spawning sub-processes
Summary(pl.UTF-8):	Powoływanie podprocesów
Name:		ocaml-spawn
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/spawn/tags
Source0:	https://github.com/janestreet/spawn/archive/v%{version}/spawn-%{version}.tar.gz
# Source0-md5:	fa54a3f1ae8cf7a565891fdc194f04e1
URL:		https://github.com/janestreet/spawn
BuildRequires:	ocaml >= 1:4.02.3
BuildRequires:	ocaml-dune >= 2.5
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spawn is a small library exposing only one functionality: spawning
sub-process.

This package contains files needed to run bytecode executables using
spawn library.

%description -l pl.UTF-8
Spawn to mała biblioteka udostępniająca tylko jedną funkcję:
powoływanie podprocesów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki spawn.

%package devel
Summary:	Spawning sub-processes - development part
Summary(pl.UTF-8):	Powoływanie podprocesów - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
spawn library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki spawn.

%prep
%setup -q -n spawn-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/spawn/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/spawn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/spawn
%{_libdir}/ocaml/spawn/META
%{_libdir}/ocaml/spawn/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/spawn/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllspawn_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/spawn/libspawn_stubs.a
%{_libdir}/ocaml/spawn/*.cmi
%{_libdir}/ocaml/spawn/*.cmt
%{_libdir}/ocaml/spawn/*.cmti
%{_libdir}/ocaml/spawn/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/spawn/spawn.a
%{_libdir}/ocaml/spawn/*.cmx
%{_libdir}/ocaml/spawn/*.cmxa
%endif
%{_libdir}/ocaml/spawn/dune-package
%{_libdir}/ocaml/spawn/opam
