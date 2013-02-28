from django import template
from canteen.menu.models import OffertimeType

register = template.Library()


@register.inclusion_tag("tags/offertime_typepe.html")
def offertime_type_list(request_path):
    type_list = OffertimeType.active.all()
    return {
        'offertime_type_list': type_list,
        'request_path': request_path
    }
