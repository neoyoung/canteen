from django import template
from canteen.menu.models import OffertimeType

register = template.Library()


@register.inclusion_tag("tags/offertime_type_link.html")
def offertime_type_list(request_path):
    pass
