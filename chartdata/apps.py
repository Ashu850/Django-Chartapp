from django.apps import AppConfig


class ChartdataConfig(AppConfig):
    name = 'chartdata'
    
    def ready(self):
        import chartdata.signals
