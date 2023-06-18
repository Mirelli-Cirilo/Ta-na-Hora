from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('api/', include('api_tanahora.urls'))
]
