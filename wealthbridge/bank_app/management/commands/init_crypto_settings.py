# wealthbridge/management/commands/init_crypto_settings.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from bank_app.models import SystemCryptoSetting  # Replace 'your_app' with your actual app name

class Command(BaseCommand):
    help = 'Initialize system crypto settings'
    
    def handle(self, *args, **options):
        settings, created = SystemCryptoSetting.objects.get_or_create(
            defaults={
                'crypto_type': 'BTC',
                'crypto_address': '3FanWZMKQrbPGj2YErdpavEumHv9qwyGfm',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✅ System crypto settings created successfully!'))
            self.stdout.write(f"   Crypto Type: {settings.crypto_type}")
            self.stdout.write(f"   Crypto Address: {settings.crypto_address}")
        else:
            self.stdout.write(self.style.WARNING('⚠️  System crypto settings already exist'))
            self.stdout.write(f"   Current Crypto Type: {settings.crypto_type}")
            self.stdout.write(f"   Current Crypto Address: {settings.crypto_address}")