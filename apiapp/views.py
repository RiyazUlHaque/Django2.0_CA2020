from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("HELLO WELCOME TO THE FIRST CUSTOM OUTPUT OF DJANGO APPLICATION")

def index1(request):
    return HttpResponse("HELLO I AM COMING FROM THE FUNCTION 2")