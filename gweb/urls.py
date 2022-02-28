from django.urls import path, include
from .import views

app_name = "gwebapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('execute/', views.execute, name='execute'),
    path('team/', views.team, name='team'),
]