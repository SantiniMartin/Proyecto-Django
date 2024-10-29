from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'pagina_de_inicio.html')

def login(request):
    print("METHOD:", request.method)
    # print("usuario:", request.POST.get("user", default=None))
    # print("contraseña:", request.POST.get("password", default=None))
    return render(request, 'login.html')