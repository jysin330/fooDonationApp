# Generated by Django 4.0.10 on 2024-01-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooDonationApp', '0011_donate_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]