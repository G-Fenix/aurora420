from django.shortcuts import render

def contactus(request):
    return render(request, 'en/contactus.html')

def contactanos(request):
    return render(request, 'spa/contactanos.html')