# Generated by Django 4.0.10 on 2024-02-08 06:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fooDonationApp', '0014_alter_receiveruser_receiver_meal'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Donate',
            new_name='DonateRecipe',
        ),
        migrations.RenameModel(
            old_name='ReceiverUser',
            new_name='ReceiverRecipe',
        ),
        migrations.RenameField(
            model_name='receiverrecipe',
            old_name='des',
            new_name='description',
        ),
    ]
