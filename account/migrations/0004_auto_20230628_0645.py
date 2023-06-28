# Generated by Django 2.1.7 on 2023-06-28 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20230628_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.TextField(null=True)),
                ('people_number', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='rank_point',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='rank_tear',
            field=models.TextField(default='코생아'),
        ),
        migrations.AddField(
            model_name='groupstudy',
            name='host_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
