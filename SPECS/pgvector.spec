%global pname vector

Name:		pgvector
Version:	0.6.2
Release:	1%{?dist}
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
%make_build %{?_smp_mflags}

%install
%make_install

#Remove header file, we don't need it right now:
%{__rm} %{buildroot}/%{_includedir}/pgsql/server/extension/%{pname}/%{pname}.h

%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{pname}.so
%{_datadir}/pgsql/extension//%{pname}.control
%{_datadir}/pgsql/extension/%{pname}*sql

%changelog
* Mon Mar 25 2024 Filip Janus <fjanus@redhat.com> - 0.6.2-1
- Initial packaging

