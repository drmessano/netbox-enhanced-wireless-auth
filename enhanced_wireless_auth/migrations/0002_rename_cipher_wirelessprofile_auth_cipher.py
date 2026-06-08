from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enhanced_wireless_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wirelessprofile',
            old_name='cipher',
            new_name='auth_cipher',
        ),
    ]
