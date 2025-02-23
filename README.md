# Enhanced Wireless Authentication for NetBox

Enhanced Wireless Authentication is a NetBox plugin that adds additional wireless authentication and encryption options to NetBox. It overrides and extends the default wireless models with custom choices for authentication types and ciphers, enabling you to better manage your wireless configurations.

Below you'll find instructions for installation, configuration, usage, and development.

## 1. Requirements

1. NetBox 4.2.x (compatible with versions 4.2.0 to 4.2.99)  
2. Python 3.10  
3. Django (as used by your NetBox installation)

## 2. Installation

1. **Clone the Plugin Repository:**

    git clone https://github.com/drmessano/enhanced_wireless_auth.git
    cd enhanced_wireless_auth

2. **Activate the NetBox Virtual Environment:**

    source /opt/netbox-4.2.1/venv/bin/activate

3. **Install the Plugin in Editable Mode:**

    pip install -e .

## 3. Configuration

1. **Add the Plugin to the NetBox Configuration:**

   Edit your NetBox configuration file (typically `configuration.py`) and add the following line to the `PLUGINS` list:

    PLUGINS = [
        'enhanced_wireless_auth',
    ]

2. **Apply Migrations:**

    python /opt/netbox/netbox/manage.py migrate enhanced_wireless_auth

3. **Restart NetBox Services:**

    sudo systemctl restart netbox  

## 4. Usage

Once installed and configured, the plugin extends the wireless models in NetBox with the following features:

- Additional authentication types (e.g., OWE, WPA2-PSK, WPA3-PSK, etc.).  
- Additional cipher options (e.g., Auto, TKIP, CCMP, etc.).  
- A custom model for managing wireless profiles.

You can access these new features via the NetBox UI or through the NetBox API.

## 5. Development

For development or further customization:

1. **Project Structure:**

       enhanced_wireless_auth/
       ├── enhanced_wireless_auth/
       │   ├── __init__.py        # Contains PluginConfig and config variable
       │   ├── apps.py            # Contains the app configuration
       │   ├── choices.py         # Contains WirelessAuthTypeChoices and WirelessAuthCipherChoices
       │   ├── models.py          # Contains the WirelessProfile model
       │   └── migrations/        # Contains migration files (e.g., 0001_initial.py)
       ├── setup.py               # Packaging file
       └── README.md              # This file

2. **Clearing Cache:**

       find . -name "*.pyc" -exec rm -f {} \;
       find . -name "__pycache__" -exec rm -rf {} \;

3. **Testing:**

       python /opt/netbox/netbox/manage.py shell

   And test imports and model queries:

       from enhanced_wireless_auth.models import WirelessProfile
       print(WirelessProfile.objects.all())

## 6. License

This project is licensed under the MIT License.

## 7. Support

For issues, questions, or contributions, please open an issue on the [GitHub repository](https://github.com/drmessano/enhanced_wireless_auth/issues).
