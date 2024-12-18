from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as views_django
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name="inicio"),
    # path('login/', views.login, name="login"),
    path('login/', views_django.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', views_django.logout_then_login, name='logout'),
    path('usuarios/', include("apps.usuarios.urls")),
    path('pacientes/', include('apps.pacientes.urls'))
    
    
]