from django.shortcuts import render
from services.models import Service
from .models import Team
# Create your views here.
services = Service.objects.all()
team = Team.objects.all()
context = {
        'services': services,
        'team': team
    }
def base_view(request):

    return render(request, 'base.html', context)
def home_view(request):

    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html', context)