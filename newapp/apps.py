from django.apps import AppConfig

#from newapp import signals


class NewappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newapp'
    #def ready(self):
    #    import newapp.signals

