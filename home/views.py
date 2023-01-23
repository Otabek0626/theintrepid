from django.shortcuts import render
from services.models import Service
# Create your views here.
services = Service.objects.all()

context = {
        'services': services
    }
def home_view(request):

    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html', context)