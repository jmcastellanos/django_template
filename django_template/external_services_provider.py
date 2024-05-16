from django.conf import settings

from django_template.environment import Environment
from django_template.external_services.paypal_service import FakeApi, PaypalApi, \
    PaypalInterface


class ExternalApisProvider:

    def get_paypal_api(self) -> PaypalInterface:
        if settings.ENVIRONMENT == Environment.local:
            return FakeApi()
        elif settings.ENVIRONMENT == Environment.development:
            return FakeApi()
        else:
            return PaypalApi()
