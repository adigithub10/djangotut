from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("This is a homepage!!")
    return render(request , 'home.html')

def about(request):
    # return HttpResponse("This is my about page!!")
    return render(request , 'about.html')
