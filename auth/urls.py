from django.urls import path

urlpatterns = [
    path('', views.auth, name='auth')
]