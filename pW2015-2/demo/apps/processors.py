from .models import Personas

def myprocessors(request):
	p = Personas.objects.get(id=1)
	dic = {'valor':p}
	return dic