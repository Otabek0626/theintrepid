from django.shortcuts import render
from .models import Service
# Create your views here.
def service(request):
    services = Service.objects.all()

    render(request, 'services.html', {'services' : services})