# Generated by Django 5.2.1 on 2025-06-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartCity', '0011_alter_cittadino_occupazione'),
    ]

    operations = [
        migrations.AddField(
            model_name='progetto',
            name='totale_voti',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
