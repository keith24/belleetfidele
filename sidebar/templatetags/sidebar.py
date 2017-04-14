from mezzanine import template

from ..models import Sidebar
register = template.Library()

@register.simple_tag
def about(prop):
	obj = Sidebar.objects.all()[0]
	return {'title':obj.title, 'text':obj.text, 'imgalt':obj.imgalt}[prop]
