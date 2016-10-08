from django.apps import AppConfig


class IdeasAppConfig(AppConfig):

    name = 'ideas'

    def ready(self):
        from ideas.signals import pre_save
