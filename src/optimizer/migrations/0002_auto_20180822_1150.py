# Generated by Django 2.1 on 2018-08-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optimizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='dimension',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='local_path',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
