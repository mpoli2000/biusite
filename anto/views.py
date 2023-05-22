from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'anto/index.html')

def clases(request):
    return render(request, 'anto/clases.html')


