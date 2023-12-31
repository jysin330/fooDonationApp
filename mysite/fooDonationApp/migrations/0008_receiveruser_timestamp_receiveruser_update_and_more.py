# Generated by Django 4.0.10 on 2024-01-07 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fooDonationApp', '0007_receiveruser_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiveruser',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receiveruser',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='receiveruser',
            name='receiver_meal',
            field=models.CharField(choices=[('aalu', 'aalu'), ('aalu paratha', 'aalu paratha'), ('kajuu', 'kajuu')], default='', max_length=30),
        ),
    ]
