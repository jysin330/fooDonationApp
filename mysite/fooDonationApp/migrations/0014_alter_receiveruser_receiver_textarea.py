# Generated by Django 4.2.4 on 2023-11-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooDonationApp', '0013_alter_receiveruser_receiver_textarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiveruser',
            name='receiver_textArea',
            field=models.TextField(),
        ),
    ]
