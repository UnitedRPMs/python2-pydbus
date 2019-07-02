%global _commit cc407c8b1d25b7e28a6d661a29f9e661b1c9b964
%global _shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python2-pydbus
Version:        0.6.0
Release:        8%{?dist}
Summary:        Pythonic DBus library

License:        LGPLv2+
URL:            https://pypi.python.org/pypi/pydbus
Source:        https://github.com/LEW21/pydbus/archive/%{_commit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:	python2-rpm-macros
BuildRequires:  python2-setuptools
Requires:       python2-gobject-base
%{?python_provide:%python_provide python2-pydbus}

BuildArch:      noarch

%description 
The pydbus module provides pythonic DBUS bindings.\
It is based on PyGI, the Python GObject Introspection bindings,\
which is the recommended way to use GLib from Python.


%prep
%autosetup -n pydbus-%{_commit} 

%build
%py2_build

%install
%py2_install

%files 
%license LICENSE
%doc README.rst
%{python2_sitelib}/pydbus-*.egg-info/
%{python2_sitelib}/pydbus/

%changelog

* Tue Jun 25 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.6.0-8
- Upstream

* Tue Jan 23 2018 Vendula Poncova <vponcova@redhat.com> - 0.6.0-4
- Drop the python2 support.

* Tue Sep 05 2017 Martin Kolman <mkolman@redhat.com> - 0.6.0-3
- add patch for DTD fix
- add patch with support for asynchronous calls (vponcova)
- add patch with support for transformation between D-Bus errors and exceptions (vponcova)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Martin Kolman <mkolman@redhat.com> - 0.6.0-1
- Initial package
