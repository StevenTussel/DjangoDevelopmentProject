from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #name = 'accounts'


    #changed to this
    name = 'basedbook_website.apps.accounts'
