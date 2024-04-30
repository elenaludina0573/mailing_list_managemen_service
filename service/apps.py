from django.apps import AppConfig



class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'
    verbose_name = 'Сервис'

    def ready(self):
        from service.scheduler import start
        start()

