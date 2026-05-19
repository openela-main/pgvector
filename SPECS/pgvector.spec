%global pname vector

Name:		pgvector
Version:	0.8.1
Release:	1%{?dist}
Summary:	Open-source vector similarity search for Postgres
License:	PostgreSQL
URL:		https://github.com/%{name}/%{name}/
Source0:	https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	make gcc
BuildRequires:	postgresql-server-devel >= 18 , postgresql-server-devel < 19
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

#Remove header file, we don't need it right now:
%{__rm} %{buildroot}/%{_includedir}/pgsql/server/extension/%{pname}/%{pname}.h
%{__rm} %{buildroot}/%{_includedir}/pgsql/server/extension/%{pname}/halfvec.h
%{__rm} %{buildroot}/%{_includedir}/pgsql/server/extension/%{pname}/sparsevec.h

%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{pname}.so
%{_datadir}/pgsql/extension//%{pname}.control
%{_datadir}/pgsql/extension/%{pname}*sql

%changelog
* Tue Nov 18 2025 Filip Janus <fjanus@redhat.com> - 0.8.1-1
- Update to 0.8.1
- Initial import for postgresql18

* Wed Mar 26 2025 Nikola Davidova <ndavidov@redhat.com> - 0.6.2-2
- Enable Portable build
- Resolves: RHEL-84405

* Mon Mar 25 2024 Filip Janus <fjanus@redhat.com> - 0.6.2-1
- Initial packaging

