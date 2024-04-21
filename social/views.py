from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


# Create your views here.
def log_out(request):
    logout(request)
    return HttpResponse('goodbye')


def profile(request):
    return HttpResponse('welcome to SHAHAB project')
