# Generated by Django 3.2.3 on 2021-05-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QR_app', '0005_alter_person_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.ManyToManyField(blank=True, to='QR_app.Status'),
        ),
    ]