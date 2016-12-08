# git archive --remote git+ssh://amanduch@file.rdu.redhat.com:/home/brq/amanduch/public_git/testing-beah.git master:client --format=tar  | gzip  > testing-beah-client-1.0.tar.gz

Name: testing-beah-client
Version: 1
Release: 1%{?dist}
Summary: Testing test under beah harness

License: GPL3
URL: https://wiki.test.redhat.com/amanduch/TestingYourTestsBeahEdition
Source0: testing-beah-client-%{version}.0.tar.gz

#BuildRequires:
Requires: git rhts-devel curl

BuildArch: noarch
%description
Testing test under beah harness
#%prep
#%setup -q


#%build
#%configure
#make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_prefix}/share/rhts-amanduch/
mkdir -p %{buildroot}%{_prefix}/libexec/rhts-amanduch/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/

tar xzvf testing-beah-client-%{version}.0.tar.gz
install -p lib/rhts-make-amanduch.include %{buildroot}%{_prefix}/share/rhts-amanduch/
install -p libexec/* %{buildroot}%{_prefix}/libexec/rhts-amanduch/
install -p etc/testing-beak.conf %{buildroot}/%{_sysconfdir}/sysconfig/

%postun
echo '#'
echo '# To make this working you need to add following line to'
echo '# /usr/share/rhts/lib/rhts-make.include or to your project Makefile:'
echo '-include /usr/share/rhts-amanduch/lib/rhts-make-amanduch.include'

%files
%dir %{_prefix}/share/rhts-amanduch
%{_prefix}/share/rhts-amanduch/*

%dir %{_prefix}/libexec/rhts-amanduch
%{_prefix}/libexec/rhts-amanduch/*
%{_sysconfdir}/sysconfig/testing-beak.conf

%changelog
* Wed Dec 07 2016 Andrej Manduch <amanduch@redhat.com> - 1-1
- initial package
