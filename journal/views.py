from django.shortcuts import render

from django.http import HttpResponse

def journal(request):
    return HttpResponse("Hello, world. You're at the journal index.")
