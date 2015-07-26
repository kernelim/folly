Name:           folly
Version:        PKG_VERSION
Release:        PKG_RELEASE%{?dist}
Summary:        Facebook Open-source Library

Group:          System Environment/Libraries
License:        Apache License Version 2.0
URL:            http://github.com/facebook/folly
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  double-conversion-devel
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  glog-devel
BuildRequires:  gtest-devel
BuildRequires:  libevent-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  python

%description
Folly is an open-source C++ library developed and used at Facebook.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       double-conversion-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build

cd folly
libtoolize --force
aclocal
autoheader
automake --force-missing --add-missing
autoconf

%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd folly
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libfolly*.so
%{_libdir}/libfolly*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/folly/*
%{_libdir}/libfolly*.a
%{_libdir}/libfolly*.la

%changelog

