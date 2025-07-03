from django.shortcuts import render

def blog(request):
    return render(request, 'en/blog.html')

def icerik(request):
    return render(request, 'spa/icerik.html')