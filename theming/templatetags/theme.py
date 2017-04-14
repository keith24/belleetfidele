from mezzanine import template
register = template.Library()

from ..models import Bootswatch

@register.simple_tag
def bootswatch():
	return Bootswatch.objects.all()[0].name.lower()
