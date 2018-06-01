from django.template import Library
from ..models import GeneralSetting, Navbar
register = Library()

@register.simple_tag
def Get_general_settings():
    """
    This function use for get general site settings from database
    and use this in views.
    """
    try:
        settings = GeneralSetting.objects.all()[0]
    except IndexError:
        """
        User does not make general setting from admin site.
        """
        settings = False
    return settings

@register.simple_tag
def Get_Navbar_Item():
    """
    This function use for get all item from navbar in database.
    """
    return Navbar.objects.all()