from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cmu.urls')),  
    path('users/', include('users.urls')), 
    path('games/', include('games.urls')) 
]
