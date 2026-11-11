%global pname vector

Name:		pgvector
Version:	0.8.7
Release:	2%{?dist}
Summary:	Open-source vector similarity search for Postgres
License:	PostgreSQL
URL:		https://github.com/%{name}/%{name}/
Source0:	https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	make gcc
BuildRequires:	postgresql-server-devel >= 16, postgresql-server-devel < 17
%{?postgresql_module_requires}

%description
Open-source vector similarity search for Postgres. Supports L2 distance,
inner product, and cosine distance

%prep
%setup -q -n %{name}-%{version}

%build
%make_build %{?_smp_mflags} OPTFLAGS=""

%install
%make_install

#Remove header files, we don't need them right now:
%{__rm} -r %{buildroot}/%{_includedir}/pgsql/server/extension/%{pname}

%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{pname}.so
%{_datadir}/pgsql/extension//%{pname}.control
%{_datadir}/pgsql/extension/%{pname}*sql

%changelog
* Mon Oct 19 2026 Filip Janus <fjanus@redhat.com> - 0.8.7-2
- Remove the whole extension header directory instead of a single
  header file, since upstream 0.8.7 installs three headers
  (vector.h, halfvec.h, sparsevec.h) instead of just vector.h, to
  avoid an unpackaged-files build failure

* Sun Oct 18 2026 RHEL Packaging Agent <redhat-ymir-agent@redhat.com> - 0.8.7-1
- CVE-2026-103484 postgresql:16/pgvector: pgvector: Arbitrary code execution via out-of-bounds write during IVFFlat index build
  execution via out-of-bounds write during IVFFlat index build
- Resolves: RHEL-275341

* Wed Mar 26 2025 Nikola Davidova <ndavidov@redhat.com> - 0.6.2-2
- Enable Portable build
- Resolves: RHEL-84405

* Mon Mar 25 2024 Filip Janus <fjanus@redhat.com> - 0.6.2-1
- Initial packaging

