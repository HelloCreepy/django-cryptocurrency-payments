# Generated by Django 3.0.5 on 2020-06-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_obm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='value',
            field=models.CharField(max_length=500, null=True),
        ),
    ]