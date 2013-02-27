from canteen.foods.models import Category
from canteen import settings


def canteen(request):
    """To show the Category as a sidebar"""
    return {
        'active_categories': Category.objects.filter(is_active=True),
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'request': request
    }
