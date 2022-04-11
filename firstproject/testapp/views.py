from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s='<h1>hello world how are you?</h1>'
    return HttpResponse(s)
