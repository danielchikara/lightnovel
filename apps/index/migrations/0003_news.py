# Generated by Django 3.0.3 on 2020-07-18 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_usernovel_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
    ]
