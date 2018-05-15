# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone


# Create your views here.
def index(request):
	 return render(request, 'base.html')

def prueba(request):
	 return render(request, 'prueba.html')

def list_render(request):
	return render(request, 'asistencia_lista.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

def register_p(request):
    error_user = False
    error_pass = False
    username = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        sec_pass = request.POST['seccond_pass']
        if User.objects.filter(username=username).exists():
            error_user = True
        if password == sec_pass:
            user = User.objects.create_user(username, password)
            return redirect('/')
        else:
            error_pass = True
    return render(request, 'registration.html', {'page':page, 'error_user':error_user, 'error_email':error_email, 'error_pass':error_pass, 'user':username, 'email':email})
