from django.db import models

class WirelessAuthTypeChoices(models.TextChoices):
    TYPE_OPEN = 'open', 'Open'
    TYPE_OWE = 'owe', 'OWE (Opportunistic Wireless Encryption)'
    TYPE_WPA2_PSK = 'wpa2-psk', 'WPA2-PSK'
    TYPE_WPA3_PSK = 'wpa3-psk', 'WPA3-PSK'
    TYPE_WPA2_WPA3_MIXED_PSK = 'wpa2-wpa3-mixed-psk', 'WPA2-PSK & WPA3-PSK (Mixed)'
    TYPE_WPA2_ENTERPRISE = 'wpa2-enterprise', 'WPA2-Enterprise'
    TYPE_WPA3_ENTERPRISE = 'wpa3-enterprise', 'WPA3-Enterprise'

class WirelessAuthCipherChoices(models.TextChoices):
    CIPHER_AUTO = 'auto', 'Auto'
    CIPHER_TKIP = 'tkip', 'TKIP'
    CIPHER_CCMP = 'ccmp', 'CCMP (AES)'
    CIPHER_GCMP = 'gcmp', 'GCMP (AES-GCM)'
    CIPHER_CCMPGCMP = 'ccmpgcmp', 'CCMP (AES) & GCMP (AES-GCM)'
    CIPHER_CCMP_256 = 'ccmp-256', 'CCMP-256 (WPA3-Enterprise Suite B)'
    CIPHER_GCMP_256 = 'gcmp-256', 'GCMP-256 (WPA3-Enterprise Suite B)'

