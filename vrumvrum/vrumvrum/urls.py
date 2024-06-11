from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('acidentes.urls')),
    path('', include ('transito.urls')),
    path('', include ('semaforo.urls')),
    path('', include ('suporte.urls')),
]
