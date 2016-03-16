from django.shortcuts import render, render_to_response, RequestContext
from django.template import RequestContext
from django.views.generic import TemplateView

# Create your views here.
def index(request):
	return render_to_response('General/index_view.html', context_instance=RequestContext(request))

def login(request):
	return render_to_response('General/login.html',context_instance=RequestContext(request))

def logout(request):
    logout(request)

class login(TemplateView):
	template_name = 'General/login.html'
		