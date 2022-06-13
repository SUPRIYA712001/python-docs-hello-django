from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello supriya , Good morning ! we are loving azure and we are happy")
