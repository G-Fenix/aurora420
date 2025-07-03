from django.shortcuts import render

def aboutus(request):
    return render(request, 'en/aboutus.html')

def sobrenosotros(request):
    return render(request, 'spa/sobrenosotros.html')