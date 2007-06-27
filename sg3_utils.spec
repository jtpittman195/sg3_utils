#
# spec file for sg3_utils
# 
# please send bugfixes or comments to dgilbert at interlog dot com
#

Summary: Utilities for SCSI devices in Linux
Name: sg3_utils
Version: 1.11
Release: 1
Packager: Douglas Gilbert <dgilbert at interlog dot com>
License: GPL/FreeBSD
Group: Utilities/System
Source: ftp://www.torque.net/sg/p/sg3_utils-1.11.tgz
Url: http://www.torque.net/sg/u_index.html
Provides: sg_utils
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root/

%description
Collection of Linux utilities for devices that use the SCSI command set.
Includes utilities to copy data based on "dd" syntax and semantics (called
sg_dd, sgp_dd and sgm_dd); check INQUIRY data and VPD pages (sg_inq); check
mode and log pages (sginfo, sg_modes and sg_logs); spin up and down
disks (sg_start); do self tests (sg_senddiag); and various other functions.
See the README and CHANGELOG files. Requires the linux kernel 2.4 series
or later. In the 2.4 series SCSI generic device names (e.g. /dev/sg0) must
be used. In the 2.6 series other device names may be used as
well (e.g. /dev/sda).

Warning: Some of these tools access the internals of your system and their
incorrect usage may render your system inoperable.

Authors:
--------
    Doug Gilbert <dgilbert at interlog dot com>
    Kurt Garloff <garloff at suse dot de>  [sg_test_rwbuff]
    Peter Allworth  [contribution to sg_dd and sgp_dd]
    Martin Schwenke <martin at meltin dot net> [contribution to sg_inq]

%package devel
Summary: Files needed for developing applications using the SCSI command set
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
sg3_utils-devel contains a static library (libsgutils.a) and header files
to support using the SCSI command set on devices in Linux.

%prep
%setup

%build
make LIBDIR=/usr/lib

%install
if [ "$RPM_BUILD_ROOT" != "/" ]; then
        rm -rf $RPM_BUILD_ROOT
fi
make install INSTDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT/usr/share/man LIBDIR=$RPM_BUILD_ROOT/usr/lib INCLUDEDIR=$RPM_BUILD_ROOT/usr/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(-,root,root) %doc CREDITS README README.sg_start
%attr(-,root,root) %doc CHANGELOG INSTALL COVERAGE
%attr(755,root,root) %{_bindir}/sg_dd
%attr(755,root,root) %{_bindir}/sg_inq
%attr(755,root,root) %{_bindir}/sg_scan
%attr(755,root,root) %{_bindir}/sg_rbuf
%attr(755,root,root) %{_bindir}/sginfo
%attr(755,root,root) %{_bindir}/sg_readcap
%attr(755,root,root) %{_bindir}/sgp_dd
%attr(755,root,root) %{_bindir}/sg_map
%attr(755,root,root) %{_bindir}/sg_turs
%attr(755,root,root) %{_bindir}/sg_test_rwbuf
%attr(755,root,root) %{_bindir}/sg_start
%attr(755,root,root) %{_bindir}/sgm_dd
%attr(755,root,root) %{_bindir}/sg_read
%attr(755,root,root) %{_bindir}/sg_reset
%attr(755,root,root) %{_bindir}/sg_modes
%attr(755,root,root) %{_bindir}/sg_logs
%attr(755,root,root) %{_bindir}/sg_senddiag
%attr(755,root,root) %{_bindir}/sg_opcodes
%attr(755,root,root) %{_bindir}/sg_persist
%attr(755,root,root) %{_bindir}/sg_write_long
%attr(755,root,root) %{_bindir}/sg_read_long
%attr(755,root,root) %{_bindir}/sg_requests
%attr(755,root,root) %{_bindir}/sg_ses
%attr(755,root,root) %{_bindir}/sg_verify
%attr(755,root,root) %{_bindir}/sg_emc_trespass
%attr(755,root,root) %{_bindir}/sg_luns
%attr(755,root,root) %{_bindir}/sg_sync
%attr(755,root,root) %{_bindir}/sg_prevent
%attr(755,root,root) %{_bindir}/sg_get_config
%attr(755,root,root) %{_libdir}/libsgutils.so
%attr(755,root,root) %{_libdir}/libsgutils.so.1
%attr(755,root,root) %{_libdir}/libsgutils.so.1.0.0
# Mandrake compresses man pages with bzip2, RedHat with gzip
%attr(-,root,root) %doc %{_mandir}/man8/sg_dd.8*
%attr(-,root,root) %doc %{_mandir}/man8/sgp_dd.8*
%attr(-,root,root) %doc %{_mandir}/man8/sgm_dd.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_read.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_map.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_scan.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_rbuf.8*
%attr(-,root,root) %doc %{_mandir}/man8/sginfo.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_readcap.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_turs.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_inq.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_test_rwbuf.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_start.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_reset.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_modes.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_logs.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_senddiag.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_opcodes.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_persist.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_write_long.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_read_long.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_requests.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_ses.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_verify.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_emc_trespass.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_luns.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_sync.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_prevent.8*
%attr(-,root,root) %doc %{_mandir}/man8/sg_get_config.8*

%files devel
%defattr(-,root,root)
%attr(644,root,root) %{_includedir}/scsi/sg_lib.h
%attr(644,root,root) %{_includedir}/scsi/sg_cmds.h
%attr(755,root,root) %{_libdir}/libsgutils.la
%attr(644,root,root) %{_libdir}/libsgutils.a
 

%changelog
* Fri Nov 26 2004 - dgilbert at interlog dot com
- add sg_sync, sg_prevent and sg_get_config; fix sg_requests
  * sg3_utils-1.11
* Sat Oct 30 2004 - dgilbert at interlog dot com
- fix read capacity (10+16), add sg_luns
  * sg3_utils-1.10
* Thu Oct 21 2004 - dgilbert at interlog dot com
- sg_requests, sg_ses, sg_verify, libsgutils(sg_lib.c+sg_cmds.c), devel rpm
  * sg3_utils-1.09
* Tue Aug 31 2004 - dgilbert at interlog dot com
- 'register+move' in sg_persist, sg_opcodes sorts, sg_write_long
  * sg3_utils-1.08
* Thu Jul 08 2004 - dgilbert at interlog dot com
- add '-fHead' to sginfo, '-i' for sg_inq, new sg_opcodes + sg_persist
  * sg3_utils-1.07
* Mon Apr 26 2004 - dgilbert at interlog dot com
- sg3_utils.spec for mandrake; more sginfo work, sg_scan, sg_logs
  * sg3_utils-1.06
* Wed Nov 12 2003 - dgilbert at interlog dot com
- sg_readcap: sizes; sg_logs: double fetch; sg_map 256 sg devices; sginfo
  * sg3_utils-1.05
* Tue May 13 2003 - dgilbert at interlog dot com
- default sg_turs '-n=' to 1, sg_logs gets '-t' for temperature, CREDITS
  * sg3_utils-1.04
* Wed Apr 02 2003 - dgilbert at interlog dot com
- 6 byte CDBs for sg_modes, sg_start on block devs, sg_senddiag, man pages
  * sg3_utils-1.03
* Wed Jan 01 2003 - dgilbert at interlog dot com
- interwork with block SG_IO, fix in sginfo, '-t' for sg_turs
  * sg3_utils-1.02
* Wed Aug 14 2002 - dgilbert at interlog dot com
- raw switch in sg_inq
  * sg3_utils-1.01
* Sun Jul 28 2002 - dgilbert at interlog dot com
- decode sg_logs pages, add dio to sgm_dd, drop "gen=1" arg, "of=/dev/null"
  * sg3_utils-1.00
* Sun Mar 17 2002 - dgilbert at interlog dot com
- add sg_modes+sg_logs for sense pages, expand sg_inq, add fua+sync to sg_dd++
  * sg3_utils-0.99
* Sat Feb 16 2002 - dgilbert at interlog dot com
- resurrect sg_reset; snprintf cleanup, time,gen+cdbsz args to sg_dd++
  * sg3_utils-0.98
* Sun Dec 23 2001 - dgilbert at interlog dot com
- move isosize to archive directory; now found in util-linux-2.10s and later
  * sg3_utils-0.97
* Fri Dec 21 2001 - dgilbert at interlog dot com
- add sgm_dd, sg_read, sg_simple4 and sg_simple16 [add mmap-ed IO support]
  * sg3_utils-0.96
* Sun Sep 15 2001 - dgilbert at interlog dot com
- sg_map can do inquiry; sg_dd, sgp_dd + sgq_dd dio help
  * sg3_utils-0.95
* Sun Apr 19 2001 - dgilbert at interlog dot com
- add sg_start, improve sginfo and sg_map [Kurt Garloff]
  * sg3_utils-0.94
* Sun Mar 5 2001 - dgilbert at interlog dot com
- add scsi_devfs_scan, add sg_include.h, 'coe' more general in sgp_dd
  * sg3_utils-0.93
* Tue Jan 16 2001 - dgilbert at interlog dot com
- clean sg_err.h include dependencies, bug fixes, Makefile in archive directory
  * sg3_utils-0.92
* Mon Dec 21 2000 - dgilbert at interlog dot com
- signals for sg_dd, man pages and additions for sg_rbuf and isosize
  * sg3_utils-0.91
* Mon Dec 11 2000 - dgilbert at interlog dot com
- Initial creation of package, containing
  * sg3_utils-0.90