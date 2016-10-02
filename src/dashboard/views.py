from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Area

def areas_list(request):
	queryset = Area.objects.all()
	context = {
		"object_list":queryset
	}

	return render(request,"areas_list.html",context)