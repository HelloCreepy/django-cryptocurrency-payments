# Generated by Django 3.0.5 on 2020-04-21 08:22

from django.db import migrations, models
import django.db.models.deletion
import obm.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('is_default', models.BooleanField(default=True, help_text='If True the node will be used as default for transaction sending.')),
                ('rpc_username', models.CharField(help_text='Username for JSON-RPC connections.', max_length=200, verbose_name='RPC username')),
                ('rpc_password', models.CharField(help_text='Password for JSON-RPC connections.', max_length=200, verbose_name='RPC password')),
                ('rpc_host', models.URLField(default='127.0.0.1', help_text='Listen for JSON-RPC connections on this IP address.', verbose_name='RPC host')),
                ('rpc_port', models.PositiveIntegerField(help_text='Listen for JSON-RPC connections on this port.', verbose_name='RPC port')),
                ('timeout', models.FloatField(default=300, help_text='Timeout for call of node JSON RPC.')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes', related_query_name='node', to='django_obm.Currency')),
            ],
            options={
                'unique_together': {('rpc_host', 'rpc_port')},
            },
            bases=(models.Model, obm.mixins.ConnectorMixin),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=500)),
                ('password', models.CharField(default='', max_length=500)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', related_query_name='address', to='django_obm.Currency')),
            ],
            options={
                'unique_together': {('value', 'currency')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txid', models.CharField(max_length=500, null=True, verbose_name='transaction id')),
                ('category', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=10, help_text='The transaction amount in currency.', max_digits=19)),
                ('block_number', models.PositiveIntegerField(help_text='Number of block that contain the transaction.', null=True)),
                ('fee', models.DecimalField(decimal_places=10, help_text="The amount of the fee in currency. This is only available for the 'send' category of transactions.", max_digits=19, null=True)),
                ('timestamp', models.PositiveIntegerField(help_text='Transaction creation or detection timestamp.', null=True)),
                ('from_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_obm.Address')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', related_query_name='transaction', to='django_obm.Node')),
                ('to_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', related_query_name='transaction', to='django_obm.Address')),
            ],
            options={
                'unique_together': {('node', 'txid')},
            },
        ),
    ]
