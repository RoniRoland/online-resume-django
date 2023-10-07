from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("Mishobbys", views.hobby, name="hobby"),
    path("contactarme", views.contacto, name="contacto"),
]
