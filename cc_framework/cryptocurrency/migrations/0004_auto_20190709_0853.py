# Generated by Django 2.2.3 on 2019-07-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocurrency', '0003_auto_20190708_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='confirmations_number',
            field=models.IntegerField(default=2, help_text='Minimum confirmations number after which a transaction will get the status "is confirmed"'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(choices=[('bitcoin-core', 'bitcoin-core')], max_length=200),
        ),
    ]