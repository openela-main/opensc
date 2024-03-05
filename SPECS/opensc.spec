%define opensc_module "OpenSC PKCS #11 Module"
%define nssdb %{_sysconfdir}/pki/nssdb

Name:           opensc
Version:        0.23.0
Release:        4%{?dist}
Summary:        Smart card library and applications

License:        LGPLv2+
URL:            https://github.com/OpenSC/OpenSC/wiki
Source0:        https://github.com/OpenSC/OpenSC/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        opensc.module
Patch1:         opensc-0.19.0-pinpad.patch
# File caching by default (#2000626)
Patch8:         %{name}-0.22.0-file-cache.patch
# https://github.com/OpenSC/OpenSC/pull/2656
Patch9:         %{name}-0.23.0-pkcs11-tool-import.patch
# https://github.com/OpenSC/OpenSC/pull/2712
Patch10:         %{name}-0.23.0-openssl-ctx.patch
# https://github.com/OpenSC/OpenSC/pull/2753
# https://github.com/OpenSC/OpenSC/commit/e8fba322a2f4d06ec5c74fe80f9e2b0e9fdefec6
# https://github.com/OpenSC/OpenSC/commit/891f10e49de1a5ee038b1cb2fb59dce40429e6c2
Patch11:         %{name}-0.23.0-openpgp.patch
# https://github.com/OpenSC/OpenSC/commit/81944d1529202bd28359bede57c0a15deb65ba8a
Patch12:        %{name}-0.23.0-cardos-pkcs15init.patch
# https://github.com/OpenSC/OpenSC/commit/bff98ff078a99e6864ba1a598fd7dc9af4a9476b
# https://github.com/OpenSC/OpenSC/commit/0875c69295ef28b45fb682b37cede58fc36b7a1a
Patch13:        %{name}-0.23.0-cache-offsets.patch
# https://github.com/OpenSC/OpenSC/commit/868f76fb31255fd3fdacfc3e476452efeb61c3e7
# https://github.com/OpenSC/OpenSC/commit/80cc5d30635f0d2c92b5099c0f9dc680d0ffce2f
Patch14:        %{name}-0.23.0-pin-bypass.patch
# https://github.com/OpenSC/OpenSC/commit/245efe608d083fd4e4ec96793fdefd218e26fde7
# https://github.com/OpenSC/OpenSC/commit/440ca666eff10cc7011901252d20f3fc4ea23651
# https://github.com/OpenSC/OpenSC/commit/41d61da8481582e12710b5858f8b635e0a71ab5e
# https://github.com/OpenSC/OpenSC/commit/88880db0307a07e33cf2e1592bb029e9c170dfea
# https://github.com/OpenSC/OpenSC/commit/638a5007a5d240d6fa901aa822cfeef94fe36e85
# https://github.com/OpenSC/OpenSC/commit/c449a181a6988cc1e8dc8764d23574e48cdc3fa6
# https://github.com/OpenSC/OpenSC/commit/5631e9843c832a99769def85b7b9b68b4e3e3959
# https://github.com/OpenSC/OpenSC/commit/e7f81d86dcdc751f4737f4b29a99bfc54d29c5c9
# https://github.com/OpenSC/OpenSC/commit/df5a176bfdf8c52ba89c7fef1f82f6f3b9312bc1
# https://github.com/OpenSC/OpenSC/commit/578aed8391ef117ca64a9e0cba8e5c264368a0ec
# https://github.com/OpenSC/OpenSC/commit/4013a807492568bf9907cfb3df41f130ac83c7b9
# https://github.com/OpenSC/OpenSC/commit/09164045facaeae193feb48d9c2fc5cc4321e8a
# https://github.com/OpenSC/OpenSC/commit/fc2c20c3f895569eeb58328bb882aec07325d3b
# https://github.com/OpenSC/OpenSC/commit/3b9129bd3cfc6ac57d5554e015c3df85f5076dc
# https://github.com/OpenSC/OpenSC/commit/bda61d0d276dc98b9d1d1e6810bbd21d19e3859
# https://github.com/OpenSC/OpenSC/commit/a4921ab23fd0853f327517636c50de947548161
# https://github.com/OpenSC/OpenSC/commit/085994384a7171c5c68f6718d9db10ed77c5af1
# https://github.com/OpenSC/OpenSC/commit/0f0985f6343eeac4044661d56807ee9286db42c
# https://github.com/OpenSC/OpenSC/commit/5f6370a35f151497838628f78111087eb8e7ff1
# https://github.com/OpenSC/OpenSC/commit/fbff25ec6c6d0ad3f8df76f57210698f7947fc3
Patch15:        %{name}-0.23.0-pkcs15init.patch
# https://github.com/OpenSC/OpenSC/commit/cde2e050ec4f2f1b7db38429aa4e9c0f4656308c
# https://github.com/OpenSC/OpenSC/commit/f1993dc4e0b33050b8f72a3558ee88b24c4063b2
Patch16:        %{name}-0.23.0-myeid-sym.patch
# https://github.com/OpenSC/OpenSC/pull/2948
# https://github.com/OpenSC/OpenSC/pull/3016
Patch17:        %{name}-0.23.0-constant-time-pkcs1.5.patch

BuildRequires:  make
BuildRequires:  pcsc-lite-devel
BuildRequires:  readline-devel
BuildRequires:  openssl-devel
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  autoconf automake libtool gcc
BuildRequires:  bash-completion
BuildRequires:  zlib-devel
# For tests
BuildRequires:  libcmocka-devel
BuildRequires:  vim-common
%if ! 0%{?rhel}
BuildRequires:  softhsm
%endif
BuildRequires:  openssl
Requires:       pcsc-lite-libs%{?_isa}
Requires:       pcsc-lite
Obsoletes:      mozilla-opensc-signer < 0.12.0
Obsoletes:      opensc-devel < 0.12.0
Obsoletes:      coolkey <= 1.1.0-36
# The simclist is bundled in upstream
Provides:       bundled(simclist) = 1.5

%description
OpenSC provides a set of libraries and utilities to work with smart cards. Its
main focus is on cards that support cryptographic operations, and facilitate
their use in security applications such as authentication, mail encryption and
digital signatures. OpenSC implements the PKCS#11 API so applications
supporting this API (such as Mozilla Firefox and Thunderbird) can use it. On
the card OpenSC implements the PKCS#15 standard and aims to be compatible with
every software/card that does so, too.


%prep
%setup -q
%patch1 -p1 -b .pinpad
%patch8 -p1 -b .file-cache
%patch9 -p1 -b .pkcs11-tool-import
%patch10 -p1 -b .ossl3context
%patch11 -p1 -b .openpgp
%patch12 -p1 -b .cardos-pkcs15init
%patch13 -p1 -b .cache-offsets
%patch14 -p1 -b .pin-bypass
%patch15 -p1 -b .pkcs15init
%patch16 -p1 -b .myeid-sym
%patch17 -p1 -b .constant-time-pkcs1

cp -p src/pkcs15init/README ./README.pkcs15init
cp -p src/scconf/README.scconf .
# No {_libdir} here to avoid multilib conflicts; it's just an example
sed -i -e 's|/usr/local/towitoko/lib/|/usr/lib/ctapi/|' etc/opensc.conf.example.in


%build
autoreconf -fvi
%ifarch %{ix86}
sed -i -e 's/opensc.conf/opensc-%{_arch}.conf/g' src/libopensc/Makefile.in
%endif
sed -i -e 's|"/lib /usr/lib\b|"/%{_lib} %{_libdir}|' configure # lib64 rpaths
%set_build_flags
CFLAGS="$CFLAGS -Wstrict-aliasing=2 -Wno-deprecated-declarations"
%configure --disable-static \
  --disable-autostart-items \
  --disable-notify \
  --disable-assert \
  --enable-pcsc \
  --enable-cmocka \
  --enable-sm
%make_build


%check
make check

%install
%make_install
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/p11-kit/modules/opensc.module

%ifarch %{ix86}
# To avoid multilib issues, move these files on 32b intel architectures
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/opensc.conf
install -Dpm 644 etc/opensc.conf $RPM_BUILD_ROOT%{_sysconfdir}/opensc-%{_arch}.conf
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/opensc.conf.5
install -Dpm 644 doc/files/opensc.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/opensc-%{_arch}.conf.5
# use NEWS file timestamp as reference for configuration file
touch -r NEWS $RPM_BUILD_ROOT%{_sysconfdir}/opensc-%{_arch}.conf
touch -r NEWS $RPM_BUILD_ROOT%{_mandir}/man5/opensc-%{_arch}.conf.5
%else
# For backward compatibility, symlink the old location to the new files
ln -s %{_sysconfdir}/opensc.conf $RPM_BUILD_ROOT%{_sysconfdir}/opensc-%{_arch}.conf
%endif

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" | xargs rm

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/opensc

# Upstream considers libopensc API internal and no longer ships
# public headers and pkgconfig files.
# Remove the symlink as nothing is supposed to link against libopensc.
rm -f $RPM_BUILD_ROOT%{_libdir}/libopensc.so
# remove the .pc file so we do not confuse users #1673139
rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc
rm -f $RPM_BUILD_ROOT%{_libdir}/libsmm-local.so

# the npa-tool builds to nothing since we do not have OpenPACE library
rm -rf %{buildroot}%{_bindir}/npa-tool
rm -rf %{buildroot}%{_mandir}/man1/npa-tool.1*

# the pkcs11-register is not applicable to Fedora/RHEL where we use p11-kit
rm -rf %{buildroot}%{_bindir}/pkcs11-register
rm -rf %{buildroot}%{_mandir}/man1/pkcs11-register.1*

# Remove the notification files
rm %{buildroot}%{_datadir}/applications/org.opensc.notify.desktop
rm %{buildroot}%{_mandir}/man1/opensc-notify.1*


%files
%doc COPYING NEWS README*

%{_datadir}/bash-completion/*

%ifarch %{ix86}
%{_mandir}/man5/opensc-%{_arch}.conf.5*
%else
%config(noreplace) %{_sysconfdir}/opensc.conf
%{_mandir}/man5/opensc.conf.5*
%endif

%config(noreplace) %{_sysconfdir}/opensc-%{_arch}.conf
# Co-owned with p11-kit so it is not hard dependency
%dir %{_datadir}/p11-kit
%dir %{_datadir}/p11-kit/modules
%{_datadir}/p11-kit/modules/opensc.module
%{_bindir}/cardos-tool
%{_bindir}/cryptoflex-tool
%{_bindir}/eidenv
%{_bindir}/iasecc-tool
%{_bindir}/gids-tool
%{_bindir}/netkey-tool
%{_bindir}/openpgp-tool
%{_bindir}/opensc-explorer
%{_bindir}/opensc-tool
%{_bindir}/opensc-asn1
%{_bindir}/piv-tool
%{_bindir}/pkcs11-tool
%{_bindir}/pkcs15-crypt
%{_bindir}/pkcs15-init
%{_bindir}/pkcs15-tool
%{_bindir}/sc-hsm-tool
%{_bindir}/dnie-tool
%{_bindir}/westcos-tool
%{_bindir}/egk-tool
%{_bindir}/goid-tool
%{_libdir}/lib*.so.*
%{_libdir}/opensc-pkcs11.so
%{_libdir}/pkcs11-spy.so
%{_libdir}/onepin-opensc-pkcs11.so
%%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/opensc-pkcs11.so
%{_libdir}/pkcs11/onepin-opensc-pkcs11.so
%{_libdir}/pkcs11/pkcs11-spy.so
%{_datadir}/opensc/
%{_mandir}/man1/cardos-tool.1*
%{_mandir}/man1/cryptoflex-tool.1*
%{_mandir}/man1/eidenv.1*
%{_mandir}/man1/gids-tool.1*
%{_mandir}/man1/goid-tool.1*
%{_mandir}/man1/iasecc-tool.1*
%{_mandir}/man1/netkey-tool.1*
%{_mandir}/man1/openpgp-tool.1*
%{_mandir}/man1/opensc-explorer.*
%{_mandir}/man1/opensc-tool.1*
%{_mandir}/man1/opensc-asn1.1*
%{_mandir}/man1/piv-tool.1*
%{_mandir}/man1/pkcs11-tool.1*
%{_mandir}/man1/pkcs15-crypt.1*
%{_mandir}/man1/pkcs15-init.1*
%{_mandir}/man1/pkcs15-tool.1*
%{_mandir}/man1/sc-hsm-tool.1*
%{_mandir}/man1/westcos-tool.1*
%{_mandir}/man1/dnie-tool.1*
%{_mandir}/man1/egk-tool.1*
%{_mandir}/man5/pkcs15-profile.5*


%changelog
* Thu Feb 08 2024 Veronika Hanulikova <vhanulik@redhat.com> - 0.23.0-4
- Fix CVE-2023-5992: Side-channel leaks while stripping encryption PKCS#1.5 padding

* Thu Nov 30 2023 Jakub Jelen <jjelen@redhat.com> - 0.23.0-3
- Fix file caching with different offsets (RHEL-4079)
- Fix CVE-2023-40660: Potential PIN bypass
- Fix CVE-2023-40661: Dynamic analyzers reports in pkcs15init
- Fix CVE-2023-4535: Out-of-bounds read in MyEID driver handling encryption using symmetric keys
- Fix CVE-2023-5992: Side-channel leaks while stripping encryption PKCS#1.5 padding

* Thu May 25 2023 Jakub Jelen <jjelen@redhat.com> - 0.23.0-2
- Fix regression in handling OpenPGP cards
- Fix CVE-2023-2977: buffer overrun in pkcs15init for cardos

* Wed Mar 08 2023 Jakub Jelen <jjelen@redhat.com> - 0.23.0-1
- Rebase to latest 0.23.0 release (#2100409)
- Use separate OpenSSL context to work better from inside of OpenSSL providers

* Fri Oct 08 2021 Jakub Jelen <jjelen@redhat.com> - 0.22.0-2
- Unbreak detection of unentrolled smart cards (#2007029)
- Enable file caching by default except for pkcs15-init (#2000626)

* Wed Aug 11 2021 Jakub Jelen <jjelen@redhat.com> - 0.22.0-1
- New upstream release (#1970534)

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.21.0-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Jul 15 2021 Jakub Jelen <jjelen@redhat.com> - 0.21.0-8
- Fix issue with handling EC keys in OpenSSL 3.0 (#1953480)

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.21.0-7
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Mon May 24 2021 Jakub Jelen <jjelen@redhat.com> - 0.21.0-6
- Build against OpenSSL 3.0 (#1953480)

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.21.0-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Thu Feb 25 2021 Jakub Jelen <jjelen@redhat.com> - 0.21.0-4
- Couple of more issues of strict aliasing (#1930652)

* Tue Feb 23 2021 Jakub Jelen <jjelen@redhat.com> - 0.21.0-3
- Unbreak with gcc11 (#1930652)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Jakub Jelen <jjelen@redhat.com> - 0.21.0-1
- New upstream release (#1884886)

* Fri Oct 30 2020 Jeff Law <law@redhat.com> - 0.20.0-9
- Fix potentially uninitialized array reference exposed by gcc-11

* Wed Aug 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.20.0-8
- Drop useless ldconfig scriptlets

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Jakub Jelen <jjelen@redhat.com> - 0.20.0-6
- Unbreak CardOS 5.x support (#1830528)

* Mon Feb 10 2020 Jakub Jelen <jjelen@redhat.com> - 0.20.0-5
- Unbreak build on gcc10 with -fno-common (#1799836)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Jakub Jelen <jjelen@redhat.com> - 0.20.0-3
- Drop the notification support for now

* Fri Jan 10 2020 Jakub Jelen <jjelen@redhat.com> - 0.20.0-2
- Cleanup spec file
- Split notify support to separate subpackage

* Thu Jan 02 2020 Jakub Jelen <jjelen@redhat.com> - 0.20.0-1
- New upstream release (#1749357)
- Fixes for various security issues identified by fuzzing (#1765223, #1765231, #1782520, #1782951, #1782956)

* Mon Sep 30 2019 Jakub Jelen <jjelen@redhat.com> - 0.19.0-8
- Correctly mention bundled simclist library
- Add missing zlib build requires (#1756326)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Jakub Jelen <jjelen@redhat.com> - 0.19.0-6
- Make OpenSC multilib again by moving the offending files on ix86 arch
- Do not ship packageconfig files to avoid inadvertent linking against pkcs11 modules (#1673139)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.19.0-5
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Jakub Jelen <jjelen@redhat.com> - 0.19.0-3
- Unbreak the RSA-PSS mechanisms
- Unbreak the signing using hashed mechanisms in CardOS and others

* Mon Oct 22 2018 Jakub Jelen <jjelen@redhat.com> - 0.19.0-2
- Fix verification after implementing RSA-PSS mechanisms
- Disable pinpad by default

* Tue Sep 25 2018 Jakub Jelen <jjelen@redhat.com> - 0.19.0-1
- New upstream release fixing various CVE-2018-16418 - 16421, 16423 - 16427
- Add support for RSA-PSS signatures

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Jakub Jelen <jjelen@redhat.com> - 0.18.0-3
- Do not add pkcs11 module to NSS after installation
  (NSS is loading p11-kit modules by default)
- Remove pkcs11-switch since there is nothing to switch to

* Mon May 21 2018 Jakub Jelen <jjelen@redhat.com> - 0.18.0-2
- Backport a fix for C_WaitForSlotEvent crash (#1579933)

* Thu May 17 2018 Jakub Jelen <jjelen@redhat.com> - 0.18.0-1
- New upstream release (#1567503)

* Wed Apr 04 2018 Jakub Jelen <jjelen@redhat.com> - 0.17.0-10
- Install the PKCS#11 modules also to the new NSS DB
- Drop the pkcs11-switch as the coolkey is gone

* Tue Apr 03 2018 Jakub Jelen <jjelen@redhat.com> - 0.17.0-9
- Improved support for CloudHSM (#1562572)

* Mon Mar 19 2018 Jakub Jelen <jjelen@redhat.com> - 0.17.0-8
- Build requires gcc
- Backport a fix for feitian tokens (#1558099)

* Fri Mar 02 2018 Jakub Jelen <jjelen@redhat.com> - 0.17.0-7
- Obsolete coolkey
- Do not report bogus errors from pkcs11-switch
- Do not delete nonexisting modules during uninstall (#1526670)

* Wed Feb 21 2018 Jakub Jelen <jjelen@redhat.com> - 0.17.0-6
- PIV: Use Cardholder name in the token label
- Avoid infinite loop when reading CAC cards
- Properly parse multi-byte length in SimpleTLV
- Support CAC Alt tokens

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Jakub Jelen <jjelen@redhat.com> - 0.17.0-4
- Allow functionality of a new Estonia ID cards (#1519751)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jakub Jelen <jjelen@redhat.com> - 0.17.0-1
- New upstream release including support for Coolkey and CAC cards

* Tue Feb 28 2017 Jakub Jelen <jjelen@redhat.com> - 0.16.0-5.20161016git0362439
- Add PKCS#11 library to the NSS DB (#1421692)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4.20161016git0362439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.16.0-3.20161016git0362439
- Rebuild for readline 7.x

* Mon Oct 31 2016 Jakub Jelen <jjelen@redhat.com> - 0.16.0-2.20161016git0362439
- Updated to latest git to address openssl 1.1.0 compilation issues (#1388895)
- Do not own /etc/bash_completion.d directory (#1303441)

* Tue Aug 02 2016 Jakub Jelen <jjelen@redhat.com> - 0.16.0-1
- New upstream release 0.16.0 (#1306071)

* Tue Jul 12 2016 Jakub Jelen <jjelen@redhat.com> - 0.15.0-6
- Add support for 2048 key length (#1350588)
- Explicitly set CKA_PRIVATE to false when writing certificates (#1272127)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.15.0-4
- Fix a crash in accessing public key (#1298669)

* Thu Nov 19 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.15.0-3
- Export PKCS#11 symbols from spy library (#1283306)

* Tue Aug  4 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.15.0-2
- Updated fix for issue with C_Initialize after fork() (#1218797)

* Tue Jul 14 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.15.0-1
- Update to 0.15.0 (#1209682)
- Solve issue with C_Initialize after fork() (#1218797)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.14.0-1
- new upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 28 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.13.0-12
- Added fix for crash when calling pkcs11-tool with an invalid module (#1071368)
- Added fix for invalid parameters passed to module by pkcs11-tool
  when importing a private key (#1071369)
- Configuration file opensc.conf was renamed to opensc-arch.conf to
  avoid multi-arch issues.

* Fri Jan 31 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.13.0-11
- Corrected installation path of opensc.module (#1060053)

* Mon Jan 06 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.13.0-10
- Applied myeid related patch (#1048576)

* Thu Jan 02 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.13.0-9
- Applied epass2003 related patch (#981462)

* Mon Dec 23 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.13.0-8
- Compile using the --enable-sm option (related but does not fix #981462)

* Wed Dec 18 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.13.0-7
- Ensure that pcsc-lite is depended on (#1029133)

* Mon Sep 23 2013 Stef Walter <stefw@redhat.com> - 0.13.0-6
- Install p11-kit config file to the right place (#999190)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Stef Walter <stefw@redhat.com> - 0.13.0-4
- Use the standard name format for p11-kit module configs
- Put the p11-kit module config is the system location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Kalev Lember <kalevlember@gmail.com> - 0.13.0-2
- Backport an upstream patch for fixing pkcs15 cert length calculation

* Thu Jan 03 2013 Milan Broz <mbroz@redhat.com> - 0.13.0-1
- Update to 0.13.0 (#890770)
- Remove no longer provided onepin-opensc-pkcs11.so.
- Add iasecc-tool, openpgp-tool and sc-hsm-tool.

* Fri Jul 27 2012 Tomas Mraz <tmraz@redhat.com> - 0.12.2-6
- Add a configuration file for p11-kit (#840504)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.2-4
- Add patch for dso

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Tomas Mraz <tmraz@redhat.com> - 0.12.2-2
- Rebuilt to fix trailing slashes in filelist from rpmbuild bug

* Tue Jul 19 2011 Kalev Lember <kalevlember@gmail.com> - 0.12.2-1
- Update to 0.12.2 (#722659)

* Wed May 18 2011 Kalev Lember <kalev@smartlink.ee> - 0.12.1-1
- Update to 0.12.1 (#705743)
- Removed BR libtool-ltdl-devel to build with glibc's libdl instead

* Tue Apr 12 2011 Tomas Mraz <tmraz@redhat.com> - 0.12.0-4
- drop multilib conflicting and duplicated doc file (#695368)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Kalev Lember <kalev@smartlink.ee> - 0.12.0-2
- Disabled asserts

* Mon Jan 03 2011 Kalev Lember <kalev@smartlink.ee> - 0.12.0-1
- Update to 0.12.0
- Removed and obsoleted mozilla-opensc-signer and opensc-devel subpackages
- Dropped patches which are now upstreamed
- It is no longer possible to build in both pcsc-lite and openct support,
  so opensc now gets built exclusively with pcsc-lite.

* Tue Dec 21 2010 Tomas Mraz <tmraz@redhat.com> - 0.11.13-6
- fix buffer overflow on rogue card serial numbers

* Tue Oct 19 2010 Tomas Mraz <tmraz@redhat.com> - 0.11.13-5
- own the _libdir/pkcs11 subdirectory (#644527)

* Tue Sep  7 2010 Tomas Mraz <tmraz@redhat.com> - 0.11.13-4
- fix build with new pcsc-lite

* Wed Aug 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.11.13-3
- build against libassuan1 (f14+)

* Wed Jun  9 2010 Tomas Mraz <tmraz@redhat.com> - 0.11.13-2
- replace file dependency (#601943)

* Tue Feb 16 2010 Kalev Lember <kalev@smartlink.ee> - 0.11.13-1
- new upstream version

* Sun Feb 14 2010 Kalev Lember <kalev@smartlink.ee> - 0.11.12-2
- Added patch to fix linking with the new --no-add-needed default (#564758)

* Mon Dec 21 2009 Kalev Lember <kalev@smartlink.ee> - 0.11.12-1
- new upstream version
- replaced %%define with %%global
- BR clean up from items not applicable to current Fedora releases

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.11.11-2
- Explicitly BR libassuan-static in accordance with the Packaging
  Guidelines (libassuan-devel is still static-only).

* Thu Nov 19 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.11-1
- new upstream version

* Tue Sep 29 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.9-2
- fix multilib conflict in the configuration file (#526269)

* Wed Sep 09 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.9-1
- new upstream version

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.8-5
- rebuilt with new openssl

* Mon Jul 27 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.8-4
- Depend on specific arch of pcsc-lite-libs (reported by Kalev Lember)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.8-2
- Rebuilt with new openct

* Mon May 11 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.8-1
- new upstream version - fixes security issue

* Fri Feb 27 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.7-1
- new upstream version - fixes CVE-2009-0368

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 0.11.6-2
- Add explicit requires for pcsc-lite-libs. Dlopen libpcsclite with the full
  soname.

* Tue Sep  2 2008 Tomas Mraz <tmraz@redhat.com> - 0.11.6-1
- Update to latest upstream, fixes CVE-2008-2235

* Thu Apr 10 2008 Hans de Goede <j.w.r.degoede@hhs.nl> - 0.11.4-5
- BuildRequire libassuan-devel instead of libassuan-static (bz 441812)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.11.4-4
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.11.4-3
- Rebuild for deps

* Wed Dec  5 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.4-2
- Rebuild.

* Mon Sep 10 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.4-1
- 0.11.4.

* Mon Aug 20 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.4-0.1.rc1
- 0.11.4-rc1, pkcs11-tool usage message fix applied upstream.
- License: LGPLv2+

* Thu Jul 26 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.3-2
- Fix pkcs11-tool usage message crash (#249702).

* Tue Jul 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.3-1
- 0.11.3.

* Sat Jun 30 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.3-0.1.pre2
- 0.11.3-pre2.

* Thu Jun 21 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.3-0.1.pre1
- 0.11.3-pre1.

* Sun May  6 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.2-2
- Add explicit build dependency on ncurses-devel.

* Sat May  5 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.2-1
- 0.11.2.

* Tue Apr 24 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.2-0.3.rc2
- 0.11.2-rc2.

* Fri Mar 23 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.2-0.3.rc1
- 0.11.2-rc1.

* Thu Mar 15 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.2-0.2.pre6
- 0.11.2-pre6.

* Tue Mar  6 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.11.2-0.2.pre4
- 0.11.2-pre4.
- Require pinentry-gui instead of the pinentry executable in signer.

* Sun Dec  3 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.2-0.1.pre3
- 0.11.2-pre3.
- Build with new libassuan.
- Don't run autotools during build.
- Adjust to readline/termcap/ncurses changes.

* Sat Oct 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.1-6
- Rebuild with new libassuan.

* Sun Oct  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.1-5
- Rebuild with new libassuan.

* Mon Oct  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.1-4
- Rebuild.

* Tue Sep 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.1-3
- Rebuild with new libassuan.

* Sat Sep  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.1-2
- Rebuild.

* Wed May 31 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.1-1
- 0.11.1.
- Avoid some multilib conflicts.

* Sun May  7 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.0-2
- Sync example paths in openct.conf with ctapi-common.
- Update URL.

* Thu May  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.0-1
- 0.11.0.

* Thu Apr 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.0-0.1.rc2
- 0.11.0-rc2.

* Sat Apr 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.11.0-0.1.rc1
- 0.11.0-rc1.

* Mon Mar  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.10.1-3
- Rebuild.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.10.1-2
- Avoid standard rpaths on lib64 archs.

* Sun Jan  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.10.1-1
- 0.10.1.

* Wed Nov  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.10.0-1
- 0.10.0.
- Adapt to modularized X.Org.

* Wed Oct 26 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.10.0-0.1.rc2
- 0.10.0-rc2.
- Install signer plugin only to plugin dir.

* Sat Oct 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.10.0-0.1.rc1
- 0.10.0-rc1.

* Wed Oct 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.10.0-0.1.beta2.rc1
- 0.10.0-beta2-rc1.
- Specfile cleanups.

* Tue Apr 26 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.6-2
- 0.9.6, build patch applied upstream.
- Package summary and description improvements.
- Drop explicit openct dependency.

* Fri Mar 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.4-3
- Fix FC4 build.
- Rename opensc-pam to pam_opensc per package naming guidelines.

* Wed Feb  9 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.4-2
- Substitute hardcoded 'lib' in OpenSSL checks for multi-lib platforms.
- Use --with-plugin-dir instead of --with-plugin-path (fixes x86_64).

* Thu Feb  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.4-1
- Drop unnecessary Epochs, pre-FC1 compat cruft, and no longer relevant
  --with(out) rpmbuild options.
- Exclude *.la.

* Wed Nov  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.4-0.fdr.1
- Update to 0.9.4, parallel build patch applied upstream.
- Patch to fix library paths and LDFLAGS.
- Don't require mozilla, but the plugin dir in signer.
- Build with dependency tracking disabled.

* Tue Jul 27 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.2-0.fdr.2
- Building the signer plugin can be disabled with "--without signer".
  Thanks to Fritz Elfert for the idea.
- Update description.

* Sun Jul 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.2-0.fdr.1
- Update to 0.9.2, old patches applied upstream.
- Add patch to fix parallel builds.
- Convert man pages to UTF-8.

* Thu Jul 22 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.1-0.fdr.1
- Update to 0.9.1 (preview).

* Thu Jul  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.9.0-0.fdr.0.1.alpha
- Update to 0.9.0-alpha.

* Sat May  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.1-0.fdr.8
- Rebuild with libassuan 0.6.5.

* Sat Jan 31 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.1-0.fdr.7
- Rebuild with libassuan 0.6.3.
- Add gdm example to PAM quickstart.

* Mon Jan 19 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.1-0.fdr.6
- Use /%%{_lib} instead of hardcoding /lib.

* Sat Dec 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.1-0.fdr.5
- Split PAM support into a subpackage.
- Rebuild with libassuan 0.6.2.

* Sun Nov 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.1-0.fdr.4
- Rebuild with libassuan 0.6.1.
- Include PAM quickstart doc snippet.

* Fri Nov 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.1-0.fdr.3
- Require OpenCT.

* Fri Oct 17 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.1-0.fdr.2
- Install example config files as documentation.

* Tue Oct 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.1-0.fdr.1
- Update to 0.8.1.

* Wed Aug 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.0-0.fdr.2
- Signer can be built with oldssl too.

* Wed Aug 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.0-0.fdr.1
- Update to 0.8.0.

* Wed Jul 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.0-0.fdr.0.2.cvs20030730
- Update to 20030730.
- Clean up %%docs.
- Include *.la (uses ltdl).
- Own the %%{_libdir}/pkcs11 directory.
- Disable signer; assuan has disappeared from the tarball :(

* Fri May 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.8.0-0.fdr.0.1.rc1
- First build.
