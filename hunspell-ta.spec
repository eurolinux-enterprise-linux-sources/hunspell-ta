Name: hunspell-ta
Summary: Tamil hunspell dictionaries
Version: 20100226
Release: 7%{?dist}
# Upstream download link is dead now
#Source: http://tamil.nrcfoss.au-kbc.org.in/files/hunspell/ta_IN-hunspell-Wordlist.tar.gz
Source: ta_IN-hunspell-Wordlist.tar.gz
Group: Applications/Text
URL: http://nrcfoss.au-kbc.org.in
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Tamil hunspell dictionaries.

%prep
%setup -q -c -n ta_IN-hunspell-wordlist

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell

cp -p ta_IN-hunspell-wordlist/*.dic ta_IN-hunspell-wordlist/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc ta_IN-hunspell-wordlist/README ta_IN-hunspell-wordlist/LICENSE ta_IN-hunspell-wordlist/Copyright
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Parag Nemade <pnemade AT redhat.com> - 20100226-6
- Resolves:rh#848848:-Source URL not working

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade AT redhat DOT com> - 20100226-4
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 08 2010 Parag <pnemade AT redhat.com> - 20100226-1
- Resolves:rh#568228 - [ta_IN]Fix license tag

* Tue Sep 29 2009 Parag <pnemade@redhat.com> - 20090929-1
- Update to new dictionary wordlist with new URL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060222-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060222-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20060222-2
- Added Copyright and fixed License tag

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20060222-1
- Initial Fedora release
