from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os

class AxisAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Account'

    def ready(self):
        User = get_user_model()

        # Load superuser credentials from environment variables
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "adminpassword")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser '{username}' created successfully")
