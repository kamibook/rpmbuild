Name:           steamp
Version:        0.1.4
Release:        1
Summary:        Steamp application

License:        GPLv3+
URL:            http://example.com/steamp
Source0:        %{name}
Source1:        example.toml
Source2:        %{name}.service

BuildArch:      x86_64

%description
Steamp is a sample application.

%define _binary_payload w9.gzdio

%prep
true

%build
true

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{SOURCE0} %{buildroot}/usr/bin/%{name}

mkdir -p %{buildroot}/etc/steamp
install -m 666 %{SOURCE1} %{buildroot}/etc/steamp/example.toml

mkdir -p %{buildroot}/etc/systemd/system
install -m 666 %{SOURCE2} %{buildroot}/etc/systemd/system/%{name}.service

%files
/usr/bin/steamp
/etc/steamp/example.toml
/etc/systemd/system/steamp.service

%pre
if systemctl is-active --quiet steamp; then
    systemctl stop steamp
fi

%post
systemctl daemon-reload

%preun
systemctl stop steamp

%postun
if [ $1 -eq 0 ]; then
    rm -rf /etc/steamp
    rm -f /etc/systemd/system/steamp.service
    systemctl daemon-reload
fi

%changelog
