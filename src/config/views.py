from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as login_django

def pagina_inicio(request):
    return render(request, 'pagina_de_inicio.html')

def login(request):
    username = ''
    se_autentico = False
    salio_mal = True
        
    if request.method == "POST":
        username = request.POST.get("user", default=None)
        contrasenia = request.POST.get("password", default=None)
        usuario = authenticate(request, username=username, password=contrasenia)
        se_autentico = True
        
        if usuario:
            login_django(request, usuario)
            salio_mal = False
            return redirect('inicio')
            
    ctx = {
        'se_autentico': se_autentico,
        'salio_mal': salio_mal,
        'username': username
    }
    return render(request, 'login.html', ctx)