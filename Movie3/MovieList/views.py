from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Movie_Name(request):
    message = "...."
    render(request, "base.html"),
    render(request, 'base2.html')
