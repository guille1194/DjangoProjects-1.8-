from django.shortcuts import render
from django.views.generic import *
from ittss.apps.subjects.models import *

import operator
from django.db.models import Q

class SearchView(ListView):
	template_name = 'search_engine/search_page.html'

	def get_queryset(self):
		query = self.request.GET.get('name')

		if query:
			words = query.split()

			return Subject.objects.filter(reduce(operator.and_, (Q(name__contains=word) for word in words)))


		return Subject.objects.all()
