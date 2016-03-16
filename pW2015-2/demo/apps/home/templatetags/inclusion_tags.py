from django import template
from apps.home.models import Personas


register = template.Library()

@register.inclusion_tag('home/inclusion.html')
def show_personas():
	p = Personas.objects.all()
	return {'personas':p}