# Generated by Django 4.2.7 on 2024-01-26 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0003_delete_currency_amount_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amount',
            name='name',
        ),
        migrations.AddField(
            model_name='amount',
            name='amount',
            field=models.OneToOneField(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]