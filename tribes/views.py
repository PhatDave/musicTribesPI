import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Tribe
from customAuth.models import User
from .helpers import is_ajax
from .sorting_strategies import *


def index_view(request):
	context = {
		'nav': 'index',
	}
	return render(request, 'tribes/index.html', context)


# TODO: Add more sorting options
def tribes_index_view(request):
	# tribe = Tribe.objects.all()[0]
	# print(tribe.getMembers())
	context = {}
	tribes = Tribe.objects.all()	
	sort_by = request.POST.get('value')
	if sort_by:
		if request.method == "POST" and is_ajax(request):
			sort_strategy = defaultOrder
			if sort_by == '1':
				sort_strategy = defaultOrder
			if sort_by == '2':
				sort_strategy = orderByNameAsc
			if sort_by == '3':
				sort_strategy = orderByNameDesc
			if sort_by == '4':
				sort_strategy = orderByNumOfMembersDesc
			if sort_by == '5':
				sort_strategy = orderByNumOfMembersAsc
			sorted_tribes = sort_strategy(tribes)
			serialized_tribes = []
			for tribe in sorted_tribes:
				serialized_tribes.append(tribe.serializeTribe())
			serialized_tribes.append(serialized_tribes.__len__())
			return JsonResponse(json.dumps(serialized_tribes), status=200, safe=False)
	else:
		context = {
			'tribes': tribes,
			'nav': 'tribes',
		}
		return render(request, 'tribes/tribes_index.html', context)
