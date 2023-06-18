from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'create-user', views.UserCreateViewSet, basename='create-user')
router.register(r'remedio-list', views.RemedioViewSet, basename='remedio-filter')
router.register(r'remedio-detail', views.RemedioDetail, basename='remedio-detail')

urlpatterns = [
    path('', include(router.urls)),
    path('api_login/', views.LoginViewSet.as_view())
]