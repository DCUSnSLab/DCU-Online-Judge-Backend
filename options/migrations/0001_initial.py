# Generated by Django 2.1.7 on 2020-02-09 05:20

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(db_index=True, unique=True)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
