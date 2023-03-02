from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'order'

    def ready(self):
        import order.signals
