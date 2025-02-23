from django.db import models
from .choices import WirelessAuthTypeChoices, WirelessAuthCipherChoices

class WirelessProfile(models.Model):
    name = models.CharField(max_length=100)
    auth_type = models.CharField(
        max_length=32,
        choices=WirelessAuthTypeChoices,
        default=WirelessAuthTypeChoices.TYPE_OPEN
    )
    cipher = models.CharField(
        max_length=32,
        choices=WirelessAuthCipherChoices,
        default=WirelessAuthCipherChoices.CIPHER_CCMP
    )

    def __str__(self):
        return f"Wireless Profile: {self.name}"

