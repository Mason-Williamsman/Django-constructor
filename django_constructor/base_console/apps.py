from django.apps import AppConfig


class BaseConsoleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_console'
