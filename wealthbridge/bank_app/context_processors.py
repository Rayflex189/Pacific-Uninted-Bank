# bank_app/context_processors.py

from .models import SystemCryptoSetting, CryptoWalletAddress, CryptoCurrency

def system_crypto_settings(request):
    """Make system crypto settings available to all templates"""
    try:
        # Get system settings
        system_settings = SystemCryptoSetting.get_settings()
        
        # Get all active crypto addresses
        active_addresses = CryptoWalletAddress.objects.filter(
            is_active=True,
            crypto__is_active=True
        ).select_related('crypto').order_by('crypto__sort_order', 'crypto__name')
        
        # Group addresses by cryptocurrency
        grouped_addresses = {}
        for addr in active_addresses:
            crypto_code = addr.crypto.code
            if crypto_code not in grouped_addresses:
                grouped_addresses[crypto_code] = {
                    'crypto': addr.crypto,
                    'addresses': []
                }
            grouped_addresses[crypto_code]['addresses'].append(addr)
        
        return {
            'system_crypto': system_settings,
            'crypto_addresses': active_addresses,
            'grouped_crypto_addresses': grouped_addresses,
            'crypto_system_settings': system_settings,
        }
    except Exception as e:
        # Return empty context if there's an error
        return {
            'system_crypto': None,
            'crypto_addresses': [],
            'grouped_crypto_addresses': {},
            'crypto_system_settings': None,
        }