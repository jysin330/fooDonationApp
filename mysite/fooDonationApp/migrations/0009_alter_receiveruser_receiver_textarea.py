# Generated by Django 4.2.6 on 2023-11-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooDonationApp', '0008_alter_receiveruser_receiver_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiveruser',
            name='receiver_textArea',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
