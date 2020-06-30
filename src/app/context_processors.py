import os
from django.conf import settings

def global_config(request):
    return {
        'GA_MEASUREMENT_ID': os.environ.get('GA_MEASUREMENT_ID'),
        'ENV': os.environ.get('DJANGO_SETTINGS_MODULE'),
        'READBACK_URL': settings.READBACK_URL
    }
