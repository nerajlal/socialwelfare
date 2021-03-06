# Generated by Django 3.1.5 on 2022-02-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_auto_20220227_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women_donation',
            old_name='disctrict',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='women_product',
            old_name='member_id',
            new_name='society_id',
        ),
        migrations.RenameField(
            model_name='women_purchase',
            old_name='disctrict',
            new_name='district',
        ),
        migrations.AddField(
            model_name='women_donation',
            name='society',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='women_members',
            name='women_id',
            field=models.IntegerField(default='3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='women_proposal',
            name='welfare',
            field=models.CharField(default='3', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='women_purchase',
            name='society',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
