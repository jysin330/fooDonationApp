# Generated by Django 4.2.6 on 2023-11-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooDonationApp', '0005_receiveruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiveruser',
            name='receiver_num',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
