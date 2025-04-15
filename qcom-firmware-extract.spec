Name: qcom-firmware-extract
Version:  1
Release:  1%{?dist}
Summary:  Script to extract Qualcomm firmware from Windows partition
BuildArch:  aarch64
License:  GPLv2+
URL: https://github.com/Radiicall/qcom-firmware-extract
Source0: qcom-firmware-extract
Source1: LICENSE
Requires: dislocker, bash, coreutils, util-linux, grep

%description
This package contains a script used to extract firmware from Qualcomm
Snapdragon X Elite powered machines such as the Thinkpad T14s Gen 6.
It serves as a temporary solution until the firmware is redistributable
under an appropriate license.

%prep
cp $RPM_SOURCE_DIR/qcom-firmware-extract .
cp $RPM_SOURCE_DIR/LICENSE .

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm755 qcom-firmware-extract %{buildroot}%{_bindir}/qcom-firmware-extract

%files
%{_bindir}/qcom-firmware-extract
%license LICENSE

%changelog
* Tue Apr 15 2025 Radical <radical@radical.fun> - 1
  * Initial release
