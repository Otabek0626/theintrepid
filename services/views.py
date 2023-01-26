from django.shortcuts import render
from .models import Service

# Create your views here.
def service(request):
    services = Service.objects.all()
    
    context = {
        'timer': 600,
        'services': services,
        'colors': ['pink', 'orange', 'green', 'red', 'blue', 'purple']
    }
    return render(request, 'services.html', context)