# Generated by Django 4.0.1 on 2022-02-14 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_register_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='city',
            new_name='district',
        ),
    ]
