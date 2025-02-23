from netbox.plugins import PluginConfig

class EnhancedWirelessAuthConfig(PluginConfig):
    name = 'enhanced_wireless_auth'
    verbose_name = 'Enhanced Wireless Authentication'
    description = 'Adds additional wireless authentication and encryption options to NetBox.'
    version = '1.1.0'

config = EnhancedWirelessAuthConfig

