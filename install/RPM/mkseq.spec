# Copyright 2017 Mapillary AB, Sweden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
Name: mkseq
# Epoch: 1
Version: 0.1.0.0
Release: 1
Vendor: Mapillary AB
URL: https://gitne.github.io/%{name}
BugURL: https://github.com/GITNE/%{name}/issues
Source0: https://github.com/GITNE/%{name}/archive/%{name}-v%{version}.tar.gz
License: Apache-2.0
Distribution: Fedora Project
Packager: GITNE <GITNE@noreply.users.github.com>
Group: Applications/Productivity
Icon: install/RPM/mapillary.gif
Summary: A tool for preparing photo sequences for upload to Mapillary
BuildArch: noarch
AutoReq: 0
Requires: bash, java >= 1.7
BuildRequires: java-devel >= 1.7, ant, p7zip
Provides: java(org.apache.commons.imaging)
%description
%{name} is a tool for basic preprocessing and optimization of sequences of
photos on the command‑line and via scripts for upload to Mapillary. It has been
developed with Mapillary users in mind who—for whatever reason—cannot or do not
want to use a mobile phone camera and a respective Mapillary app to take photos
for upload to Mapillary. Whatever the reason, photos which have not been shot
with the Mapillary app may require or would benefit of some preprocessing or
optimization prior to upload.

%define appid com.mapillary.%{name}

#%%prep

#%%build

#%%pre

%install
%define _appdatadir %{_datadir}/appdata
%{__install} -o root -g root -m 0755 -D %{_sourcedir}/install/usr/bin/%{name} %{buildroot}%{_bindir}/%{name}
%{__install} -o root -g root -m 0644 -D %{_sourcedir}/dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
%{__install} -o root -g root -m 0644 -D %{_sourcedir}/lib/commons-imaging.jar %{buildroot}%{_javadir}/commons-imaging.jar
%{__install} -o root -g root -m 0644 -D %{_sourcedir}/LICENSE %{buildroot}%{_defaultdocdir}/%{name}/LICENSE
%{__install} -o root -g root -m 0644 -D %{_sourcedir}/install/usr/share/appdata/%{appid}.appdata.xml %{buildroot}%{_appdatadir}/%{appid}.appdata.xml
%{__install} -o root -g root -m 0644 -D %{_sourcedir}/install/usr/share/applications/%{appid}.desktop %{buildroot}%{_datadir}/applications/%{appid}.desktop
%{__install} -o root -g root -m 0644 -D %{_sourcedir}/install/usr/share/icons/hicolor/scalable/actions/mapillaryaction.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/actions/mapillaryaction.svg
%{__install} -o root -g root -m 0644 -D %{_sourcedir}/install/usr/share/icons/hicolor/scalable/apps/mapillary.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mapillary.svg
%{__7zip} a -tgzip -mx=9 %{_sourcedir}/doc/man/en/man1/%{name}.1.gz %{_sourcedir}/doc/man/en/man1/%{name}.1 > /dev/null
%{__install} -o root -g root -m 0644 -D %{_sourcedir}/doc/man/en/man1/%{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

#%%post

#%%preun

#%%postun

%files
%define _binary_payload w9.gzdio
%define _binary_filedigest_algorithm 2
%defattr(-,root,root,644)
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/commons-imaging.jar
%{_javadir}/%{name}.jar
%{_appdatadir}/%{appid}.appdata.xml
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/scalable/actions/mapillaryaction.svg
%{_datadir}/icons/hicolor/scalable/apps/mapillary.svg

%doc
%license %{_defaultdocdir}/%{name}/LICENSE
%lang(en) %{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Apr 5 2017 GITNE <GITNE@noreply.users.github.com> 0.1.0.0-1
- Initial %{name} release
