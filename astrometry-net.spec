Name:      astrometry-net
Version:   0.97
Release:   1%{dist}
Url:       https://github.com/rockit-astro/astrometry-net-packaging
Summary:   Astrometry.net repackaged for Rocky Linux
License:   BSD
Group:     Unspecified
BuildRequires: cairo-devel libpng-devel libjpeg-turbo-devel zlib-devel bzip2-devel swig netpbm netpbm-devel netpbm-progs cfitsio-devel python3-devel python3-numpy gcc make
Requires: cfitsio netpbm-progs python3-numpy python3-astropy
BuildArch: x86_64 aarch64

%description

Astrometry.net repackaged for Rocky Linux.

%build

tar xf %{_sourcedir}/astrometry.net-0.97.tar.gz --strip-components=1

make
make install INSTALL_DIR=%{buildroot}/%{_prefix} LIB_INSTALL_DIR=%{buildroot}/%{_libdir} ETC_INSTALL_DIR=%{buildroot}/%{_sysconfdir} DATA_INSTALL_DIR=%{buildroot}/%{_sysconfdir}/astrometry DATA_FINAL_DIR=%{_sysconfdir}/astrometry PY_BASE_INSTALL_DIR=%{buildroot}/%{python3_sitearch}/astrometry

rm -rf %{buildroot}/usr/doc %{buildroot}/usr/examples %{buildroot}/%{_libdir}/*.a %{buildroot}/%{_includedir}
%files
%defattr(0755,root,root,0755)
%{_bindir}/*

%defattr(0644,root,root,0644)
%{_sysconfdir}/astrometry.cfg
%{_libdir}/*.so
%{_mandir}/man1/*.1

%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
