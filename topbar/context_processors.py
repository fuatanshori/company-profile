from .models import TopBar
from plnnusantarapower.utils import get_data_or_none

def topbarutils(request):
    topbar      = get_data_or_none(TopBar)
    context = {
        'topbar_email':topbar.email if topbar else None,
        'topbar_phone_number':topbar.phone_number if topbar else None,
        'topbar_socials':topbar.social.all() if topbar else None, 
    }
    return context