# Generated by Django 3.0.3 on 2020-07-25 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20200720_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usernovel',
            name='rol_user',
        ),
        migrations.AddField(
            model_name='user',
            name='rol_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rol_users', to='index.RolUser'),
        ),
    ]
