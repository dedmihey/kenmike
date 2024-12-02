from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index11(request):
    return render(request, 'third_task/hauptseite.html')

def index12(request):
    return render(request, 'third_task/kesseln.html')

def index13(request):
    return render(request, 'third_task/korb.html')
