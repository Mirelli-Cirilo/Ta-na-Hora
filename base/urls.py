from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('envio_email/', views.envio_email, name='email')
]