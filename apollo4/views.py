# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http  import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'apollo4/index.html')


@csrf_exempt
def data(request):
	print("i am here")
	if request.method == "POST":
		get_value= request.body
		print (get_value)
		return HttpResponse("patent")
