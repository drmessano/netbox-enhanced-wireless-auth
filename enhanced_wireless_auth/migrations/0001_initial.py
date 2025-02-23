from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='WirelessProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('auth_type', models.CharField(
                    max_length=32, choices=[
                        ('open', 'Open'),
                        ('owe', 'OWE'),
                        ('wpa2-psk', 'WPA2-PSK'),
                        ('wpa3-psk', 'WPA3-PSK'),
                        ('wpa2-wpa3-mixed-psk', 'WPA2-PSK & WPA3-PSK (Mixed)'),
                        ('wpa2-enterprise', 'WPA2-Enterprise'),
                        ('wpa3-enterprise', 'WPA3-Enterprise')
                    ], default='open')),
                ('cipher', models.CharField(
                    max_length=32, choices=[
                        ('auto', 'Auto'),
                        ('tkip', 'TKIP'),
                        ('ccmp', 'CCMP (AES)'),
                        ('gcmp', 'GCMP (AES-GCM)'),
                        ('ccmpgcmp', 'CCMP (AES) & GCMP (AES-GCM)'),
                        ('ccmp-256', 'CCMP-256 (WPA3-Enterprise Suite B)'),
                        ('gcmp-256', 'GCMP-256 (WPA3-Enterprise Suite B)')
                    ], default='auto')),
            ],
        ),
    ]

