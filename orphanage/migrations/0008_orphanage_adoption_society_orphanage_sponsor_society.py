# Generated by Django 4.0 on 2022-03-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0007_rename_disctrict_orphanage_purchase_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='orphanage_adoption',
            name='society',
            field=models.CharField(default='orphanage1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orphanage_sponsor',
            name='society',
            field=models.CharField(default='orphanage1', max_length=50),
            preserve_default=False,
        ),
    ]
