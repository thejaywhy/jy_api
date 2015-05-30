"""
This module custom context processors
"""
from django.conf import settings

GOOGLE_ANALYTICS = settings.GOOGLE_ANALYTICS

def get_analytics_id(request):
    """
    Get Google Analytics ID from settings
    """
    return {
        'ga_id': GOOGLE_ANALYTICS['id'],
        'ga_domain': GOOGLE_ANALYTICS['domain']
    }
