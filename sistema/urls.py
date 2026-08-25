from django.contrib import admin
from django.urls import path
from cadastro import views as cadastro_view
from login import views as login_view
from app import views as app_view
from painel import views as painel_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_view.home, name='home'),
    path('cadastro/', cadastro_view.cadastro, name='cadastro'),
    path('ativar/<uidb64>/<token>/', cadastro_view.ativar_conta, name='ativar_conta'),
    path('login/', login_view.login_view, name='login'),
    path('painel/', painel_view.painel_principal, name='painel'),
    path('logout/', login_view.logout_view, name='logout'),
]