from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "single/index.html")

def result(request):
    return render(request, "single/result.html")
