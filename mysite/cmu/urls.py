from django.urls import path

from . import views

app_name = 'cmu'

urlpatterns = [
    path('', views.main, name='main'), 
    path('main-page/', views.index, name='index')
]