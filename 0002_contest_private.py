# Generated by Django 2.2.16 on 2020-09-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]

