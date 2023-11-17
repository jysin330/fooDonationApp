# Generated by Django 4.2.6 on 2023-11-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooDonationApp', '0004_alter_donate_address_alter_donate_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='category',
            field=models.CharField(choices=[('Raw Food', 'Raw Food'), ('Packed Food', 'Packed Food'), ('Cooked Food', 'Cooked Food')], default='1', max_length=30),
        ),
    ]