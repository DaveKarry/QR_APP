# Generated by Django 3.2.3 on 2021-05-26 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QR_app', '0016_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='creationDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
