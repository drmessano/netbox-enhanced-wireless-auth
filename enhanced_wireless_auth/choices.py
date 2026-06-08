from utilities.choices import ChoiceSet


class WirelessAuthTypeChoices(ChoiceSet):
    TYPE_OPEN = 'open'
    TYPE_OWE = 'owe'
    TYPE_WPA2_PSK = 'wpa2-psk'
    TYPE_WPA3_PSK = 'wpa3-psk'
    TYPE_WPA2_WPA3_MIXED_PSK = 'wpa2-wpa3-mixed-psk'
    TYPE_WPA2_ENTERPRISE = 'wpa2-enterprise'
    TYPE_WPA3_ENTERPRISE = 'wpa3-enterprise'

    CHOICES = [
        (TYPE_OPEN, 'Open'),
        (TYPE_OWE, 'OWE (Opportunistic Wireless Encryption)'),
        (TYPE_WPA2_PSK, 'WPA2-PSK'),
        (TYPE_WPA3_PSK, 'WPA3-PSK'),
        (TYPE_WPA2_WPA3_MIXED_PSK, 'WPA2-PSK & WPA3-PSK (Mixed)'),
        (TYPE_WPA2_ENTERPRISE, 'WPA2-Enterprise'),
        (TYPE_WPA3_ENTERPRISE, 'WPA3-Enterprise'),
    ]


class WirelessAuthCipherChoices(ChoiceSet):
    CIPHER_AUTO = 'auto'
    CIPHER_TKIP = 'tkip'
    CIPHER_CCMP = 'ccmp'
    CIPHER_GCMP = 'gcmp'
    CIPHER_CCMPGCMP = 'ccmpgcmp'
    CIPHER_CCMP_256 = 'ccmp-256'
    CIPHER_GCMP_256 = 'gcmp-256'

    CHOICES = [
        (CIPHER_AUTO, 'Auto'),
        (CIPHER_TKIP, 'TKIP'),
        (CIPHER_CCMP, 'CCMP (AES)'),
        (CIPHER_GCMP, 'GCMP (AES-GCM)'),
        (CIPHER_CCMPGCMP, 'CCMP (AES) & GCMP (AES-GCM)'),
        (CIPHER_CCMP_256, 'CCMP-256 (WPA3-Enterprise Suite B)'),
        (CIPHER_GCMP_256, 'GCMP-256 (WPA3-Enterprise Suite B)'),
    ]
