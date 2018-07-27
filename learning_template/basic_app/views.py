from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'word': 'Hello World','date' : 2018}
    return render(request, 'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')
