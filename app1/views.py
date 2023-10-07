from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "base.html")


def hobby(request):
    return render(request, "hobby.html")


def contacto(request):
    return render(request, "contacto.html")
