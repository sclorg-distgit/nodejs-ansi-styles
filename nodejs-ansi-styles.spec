%{?scl:%scl_package nodejs-ansi-styles}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       %{?scl_prefix}nodejs-ansi-styles
Version:    2.2.1
Release:    1%{?dist}
Summary:    ANSI escape codes for colorizing strings in the terminal
License:    MIT
URL:        https://github.com/chalk/ansi-styles
Source0:    http://registry.npmjs.org/ansi-styles/-/ansi-styles-%{version}.tgz
Source1:    https://raw.githubusercontent.com/chalk/ansi-styles/95c59b23be760108b6530ca1c89477c21b258032/test.js

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n package
cp -p %{SOURCE1} .

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ansi-styles
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/ansi-styles

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
/usr/bin/mocha
%endif

%files
%doc license readme.md
%{nodejs_sitelib}/ansi-styles

%changelog
* Tue Sep 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com>
- Update, update URL and test

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.0-5
- Use macro in -runtime dependency
- Rebuilt with updated metapackage

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 2.1.0-2
- Enable scl macros

* Mon Sep 14 2015 Troy Dawson <tdawson@redhat.com> - 2.1.0-4
- UPdate to 2.1.0
- Remove tests until all dependencies are built

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-1
- initial package
