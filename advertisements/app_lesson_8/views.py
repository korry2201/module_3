from django.http import HttpResponse   
from django.shortcuts import render

def new_response(request):
    return HttpResponse('Домашка по 8 занятию')

