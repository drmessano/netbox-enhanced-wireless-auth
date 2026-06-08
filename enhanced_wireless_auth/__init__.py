from netbox.plugins import PluginConfig


class EnhancedWirelessAuthConfig(PluginConfig):
    name = 'enhanced_wireless_auth'
    verbose_name = 'Enhanced Wireless Authentication'
    description = 'Adds additional wireless authentication and encryption options to NetBox.'
    version = '1.6.0'
    min_version = '4.2.0'
    max_version = '4.6.99'
    author = 'Danny Messano'
    author_email = 'drmessano@gmail.com'

    def ready(self):
        from .choices import WirelessAuthTypeChoices, WirelessAuthCipherChoices
        import wireless.choices as wireless_choices

        # Mutate _choices on the original NetBox ChoiceSet class objects.
        # Every reference across NetBox (model fields, table columns, filtersets)
        # points to the same class object in memory. ChoiceSetMeta.__iter__
        # returns cls._choices, so this single mutation propagates everywhere.
        wireless_choices.WirelessAuthTypeChoices._choices = list(WirelessAuthTypeChoices)
        wireless_choices.WirelessAuthCipherChoices._choices = list(WirelessAuthCipherChoices)

        # Form base_fields store a frozen list (not the class reference) —
        # overwrite the list directly.
        auth_type_choices = [('', '---------')] + list(WirelessAuthTypeChoices)
        auth_cipher_choices = [('', '---------')] + list(WirelessAuthCipherChoices)
        from wireless.forms import WirelessLANForm, WirelessLinkForm
        for form in (WirelessLANForm, WirelessLinkForm):
            form.base_fields['auth_type'].choices = auth_type_choices
            form.base_fields['auth_cipher'].choices = auth_cipher_choices

        # API serializer ChoiceField builds its own _choices dict at __init__ time.
        try:
            from wireless.api.serializers import WirelessLANSerializer, WirelessLinkSerializer
            type_dict = dict(list(WirelessAuthTypeChoices))
            cipher_dict = dict(list(WirelessAuthCipherChoices))
            for serializer in (WirelessLANSerializer, WirelessLinkSerializer):
                serializer._declared_fields['auth_type']._choices = type_dict
                serializer._declared_fields['auth_cipher']._choices = cipher_dict
        except (ImportError, KeyError):
            pass


config = EnhancedWirelessAuthConfig
