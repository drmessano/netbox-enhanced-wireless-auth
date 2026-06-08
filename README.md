# Enhanced Wireless Authentication for NetBox

A NetBox plugin that extends the built-in wireless models with additional authentication types and cipher options, enabling more complete wireless configuration management.

## Compatibility

| Plugin version | NetBox version |
|----------------|----------------|
| 1.6.x          | 4.2 – 4.6      |
| 1.1.x          | 4.2            |

**Requirements:** Python 3.12+

## Features

- Extended authentication types: Open, OWE, WPA2-PSK, WPA3-PSK, WPA2/WPA3 Mixed, WPA2-Enterprise, WPA3-Enterprise
- Extended cipher options: Auto, TKIP, CCMP (AES), GCMP (AES-GCM), CCMP+GCMP, CCMP-256, GCMP-256
- Custom `WirelessProfile` model for managing named wireless configs

## Installation

### Production

Activate the NetBox virtual environment, then install directly from GitHub:

```bash
source /opt/netbox/venv/bin/activate
pip install https://github.com/drmessano/netbox-enhanced-wireless-auth/archive/refs/heads/main.zip
```

Or clone and install:

```bash
git clone https://github.com/drmessano/netbox-enhanced-wireless-auth.git
source /opt/netbox/venv/bin/activate
pip install ./netbox-enhanced-wireless-auth
```

### Development (editable install)

```bash
git clone https://github.com/drmessano/netbox-enhanced-wireless-auth.git
cd netbox-enhanced-wireless-auth
source /opt/netbox/venv/bin/activate
pip install -e .
```

## Configuration

1. Add the plugin to your NetBox `configuration.py`:

```python
PLUGINS = [
    'enhanced_wireless_auth',
]
```

2. Apply migrations:

```bash
python /opt/netbox/netbox/manage.py migrate enhanced_wireless_auth
```

3. Restart NetBox:

```bash
sudo systemctl restart netbox netbox-rq
```

## Project Structure

```
netbox-enhanced-wireless-auth/
├── enhanced_wireless_auth/
│   ├── __init__.py        # PluginConfig
│   ├── apps.py            # AppConfig
│   ├── choices.py         # Auth type and cipher choice classes
│   ├── models.py          # WirelessProfile model
│   └── migrations/
│       └── 0001_initial.py
├── pyproject.toml
└── README.md
```

## Development

Clear compiled bytecode:

```bash
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
```

Test in the NetBox shell:

```bash
python /opt/netbox/netbox/manage.py shell
```

```python
from enhanced_wireless_auth.models import WirelessProfile
WirelessProfile.objects.all()
```

## License

MIT

## Support

Open an issue on [GitHub](https://github.com/drmessano/netbox-enhanced-wireless-auth/issues).
