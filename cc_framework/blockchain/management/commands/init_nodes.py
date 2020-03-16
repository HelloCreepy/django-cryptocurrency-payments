from django.conf import settings
from django.core.management.base import BaseCommand

from cc_framework.blockchain import models


class Command(BaseCommand):
    help = 'Creates nodes and currencies objects from initial config.'

    def get_or_create_with_stdout(self, model, defaults=None, **kwargs):
        obj, created = model.objects.get_or_create(
            **kwargs,
            defaults=defaults or {},
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'{repr(obj)} created successfully.'))
        return obj

    def handle(self, *args, **options):
        for node_config in getattr(settings, 'INITIAL_NODES_CONFIG', []):
            currency_config = node_config.pop('currency')
            node_config['currency'] = self.get_or_create_with_stdout(
                model=models.Currency,
                name=currency_config.pop('name'),
                defaults=currency_config,
            )
            self.get_or_create_with_stdout(model=models.Node, **node_config)
