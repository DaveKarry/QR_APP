# Generated by Django 3.2.3 on 2021-05-22 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QR_app', '0010_status_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='status',
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='QR_app.status'),
            preserve_default=False,
        ),
    ]
