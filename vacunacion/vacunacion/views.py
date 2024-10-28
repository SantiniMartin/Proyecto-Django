from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'pagina_de_inicio.html')

def login(request):
    print("METHOD:", request.method)
    return render(request, 'login.html')