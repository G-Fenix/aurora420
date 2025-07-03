from django.shortcuts import render

def events(request):
    return render(request, 'en/events.html')

def paintpufmonday(request):
    return render(request, 'en/paintpufmonday.html')

def highflixtuesday(request):
    return render(request, 'en/highflixtuesday.html')

def weedwisdomwednesday(request):
    return render(request, 'en/weedwisdomwednesday.html')

def talkitthursday(request):
    return render(request, 'en/talkitthursday.html')

def gamerushfriday(request):
    return render(request, 'en/gamerushfriday.html')

def openmicsaturday(request):
    return render(request, 'en/openmicsaturday.html')

def eventos(request):
    return render(request, 'spa/eventos.html')

def lunesdepintura(request):
    return render(request, 'spa/lunesdepintura.html')

def martesdehighflix(request):
    return render(request, 'spa/martesdehighflix.html')

def miercolesdesabiduria(request):
    return render(request, 'spa/miercolesdesabiduria.html')

def juevesdeconserva(request):
    return render(request, 'spa/juevesdeconserva.html')

def viernesdejuegos(request):
    return render(request, 'spa/viernesdejuegos.html')

def sabadodemicrofono(request):
    return render(request, 'spa/sabadodemicrofono.html')