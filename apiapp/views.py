from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context={
        "data": "Hello I am doing something funny with my Django Template",
        "list_Seq": [10,20,30,40,50,60,70,80,90,100]
    }
    return render(request,"index.html",context)

def index1(request):
    return HttpResponse("HELLO I AM COMING FROM THE FUNCTION 2")