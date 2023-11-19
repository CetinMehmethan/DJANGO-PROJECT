from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')
def iletisim(request):
    return render(request,'iletisim.html')
def hakkimizda(request):
    return render(request,'hakkimizda.html')