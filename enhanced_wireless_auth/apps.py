from django.apps import AppConfig

class EnhancedWirelessAuthConfig(AppConfig):
    name = 'enhanced_wireless_auth'
    verbose_name = 'Enhanced Wireless Authentication'

    def ready(self):
        from .choices import WirelessAuthTypeChoices, WirelessAuthCipherChoices
