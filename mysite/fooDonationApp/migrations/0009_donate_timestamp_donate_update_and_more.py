# Generated by Django 4.0.10 on 2024-01-08 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fooDonationApp', '0008_receiveruser_timestamp_receiveruser_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donate',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='receiveruser',
            name='receiver_meal',
            field=models.CharField(default='', max_length=30),
        ),
    ]