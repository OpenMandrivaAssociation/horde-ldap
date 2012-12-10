%define prj Horde_LDAP

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-ldap
Version:       0.0.2
Release:       %mkrel 4
Summary:       LDAP Utility Class
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-framework
Requires:      php-pear
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
Horde_LDAP:: contains some utility functions for dealing with LDAP servers
and data.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%{peardir}/Horde/LDAP.php
%dir %{peardir}/tests/Horde_LDAP
%dir %{peardir}/tests/Horde_LDAP/tests
%{peardir}/tests/Horde_LDAP/tests/quoteDN.phpt




%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-4mdv2011.0
+ Revision: 564075
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2010.1
+ Revision: 523071
- increased release version
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Sat Feb 27 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 512391
- bumped up release
- corrected spelling
- replaced PreReq with Requires(pre)
- removed BuildRequires: horde-framework
- Initial import


