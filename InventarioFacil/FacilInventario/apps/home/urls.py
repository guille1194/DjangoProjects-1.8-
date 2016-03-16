from django.conf.urls import url
from .views import Index_view, Test_view

urlpatterns = [
	url(r'^$', Index_view.as_view(), name='index_view'),
	url(r'^test/$', Test_view, name='Test_view'),
]