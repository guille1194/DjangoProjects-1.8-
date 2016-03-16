from django.conf.urls import patterns, include, url
from django.contrib import admin

from ittss.apps.search_engine.views import *
from ittss.apps.subjects.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ittss.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', SearchView.as_view(), name='search_view'),
    url(r'^subjects/(?P<pk>\d+)/$', SubjectView.as_view(), name="subject_view"),
    url(r'^subjects/add/$', CreateSubjectView.as_view(), name="create_subject_view"),
)
