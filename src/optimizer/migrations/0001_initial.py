# Generated by Django 2.1 on 2018-08-21 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=200, validators=[django.core.validators.URLValidator()])),
                ('quality', models.IntegerField()),
                ('dimension', models.FloatField(blank=True)),
                ('local_path', models.CharField(editable=False, max_length=50)),
            ],
        ),
    ]
