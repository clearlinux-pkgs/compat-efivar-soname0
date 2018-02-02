#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-efivar-soname0
Version  : 0.21
Release  : 5
URL      : https://github.com/rhinstaller/efivar/releases/download/0.21/efivar-0.21.tar.bz2
Source0  : https://github.com/rhinstaller/efivar/releases/download/0.21/efivar-0.21.tar.bz2
Summary  : Tools to manage UEFI variables
Group    : Development/Tools
License  : LGPL-2.1
Requires: compat-efivar-soname0-bin
Requires: compat-efivar-soname0-lib
Requires: compat-efivar-soname0-doc
BuildRequires : popt-dev
Patch1: build.patch
Patch2: nvme.patch

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package bin
Summary: bin components for the compat-efivar-soname0 package.
Group: Binaries

%description bin
bin components for the compat-efivar-soname0 package.


%package dev
Summary: dev components for the compat-efivar-soname0 package.
Group: Development
Requires: compat-efivar-soname0-lib
Requires: compat-efivar-soname0-bin
Provides: compat-efivar-soname0-devel

%description dev
dev components for the compat-efivar-soname0 package.


%package doc
Summary: doc components for the compat-efivar-soname0 package.
Group: Documentation

%description doc
doc components for the compat-efivar-soname0 package.


%package lib
Summary: lib components for the compat-efivar-soname0 package.
Group: Libraries

%description lib
lib components for the compat-efivar-soname0 package.


%prep
%setup -q -n efivar-0.21
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494609268
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1494609268
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/efivar

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/efivar/efiboot-creator.h
%exclude /usr/include/efivar/efiboot-loadopt.h
%exclude /usr/include/efivar/efiboot.h
%exclude /usr/include/efivar/efivar-dp.h
%exclude /usr/include/efivar/efivar-guids.h
%exclude /usr/include/efivar/efivar.h
%exclude /usr/lib64/libefiboot.so
%exclude /usr/lib64/libefivar.so
%exclude /usr/lib64/pkgconfig/efiboot.pc
%exclude /usr/lib64/pkgconfig/efivar.pc

%files doc
%defattr(-,root,root,-)
%exclude /usr/share/man/man1/efivar.1
%exclude /usr/share/man/man3/efi_append_variable.3
%exclude /usr/share/man/man3/efi_del_variable.3
%exclude /usr/share/man/man3/efi_get_next_variable_name.3
%exclude /usr/share/man/man3/efi_get_variable.3
%exclude /usr/share/man/man3/efi_get_variable_attributes.3
%exclude /usr/share/man/man3/efi_get_variable_size.3
%exclude /usr/share/man/man3/efi_guid_to_id_guid.3
%exclude /usr/share/man/man3/efi_guid_to_name.3
%exclude /usr/share/man/man3/efi_guid_to_str.3
%exclude /usr/share/man/man3/efi_guid_to_symbol.3
%exclude /usr/share/man/man3/efi_name_to_guid.3
%exclude /usr/share/man/man3/efi_set_variable.3
%exclude /usr/share/man/man3/efi_str_to_guid.3
%exclude /usr/share/man/man3/efi_symbol_to_guid.3
%exclude /usr/share/man/man3/efi_variable_alloc.3
%exclude /usr/share/man/man3/efi_variable_export.3
%exclude /usr/share/man/man3/efi_variable_free.3
%exclude /usr/share/man/man3/efi_variable_get_attributes.3
%exclude /usr/share/man/man3/efi_variable_get_data.3
%exclude /usr/share/man/man3/efi_variable_get_guid.3
%exclude /usr/share/man/man3/efi_variable_get_name.3
%exclude /usr/share/man/man3/efi_variable_import.3
%exclude /usr/share/man/man3/efi_variable_realize.3
%exclude /usr/share/man/man3/efi_variable_set_attributes.3
%exclude /usr/share/man/man3/efi_variable_set_data.3
%exclude /usr/share/man/man3/efi_variable_set_guid.3
%exclude /usr/share/man/man3/efi_variable_set_name.3
%exclude /usr/share/man/man3/efi_variable_t.3
%exclude /usr/share/man/man3/efi_variables_supported.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libefiboot.so.0
/usr/lib64/libefiboot.so.0.21
/usr/lib64/libefivar.so.0
/usr/lib64/libefivar.so.0.21
