from .models import Student, Perfil
import django
import sys


def user_image(request):
	try:
		img = None
		user = request.user
		up = Perfil.objects.get(user_perfil=user)
		#print up
		img = 'http://localhost:8000/media/%s'%up.image
	except:
		img = 'http://localhost:8000/media/debian.jpg'
	return img

def myprocessors(request):
	get_version_django = django.get_version()
	get_version_python = sys.version
	p = Student.objects.get(id=1)
	dic = {'valor':p, 'get_image_profile':user_image(request), 'django_version': get_version_django, 'python_version': get_version_python}
	return dic