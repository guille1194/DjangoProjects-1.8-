from .models import Personas, Perfiles


def user_image(request):
	try:
		img = None
		user = request.user
		up = Perfiles.objects.get(user_perfil=user)
		img = '/media/%s'%up.image
	except:
		img = '/media/user_image/debian.jpg'
	return img

def myprocessors(request):
	p = Personas.objects.get(id=1)
	dic = {'valor':p, 'get_image_profile':user_image(request)}
	return dic