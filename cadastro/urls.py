from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout')
]