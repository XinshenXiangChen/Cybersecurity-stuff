from django.apps import AppConfig


class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Full Python path to the app so Django can import it correctly
    name = 'users_app'
