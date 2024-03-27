from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.main, name='main'), 
    path("main/<int:page>", views.main, name = "main_paginate"),
    path('my-games/', views.my_games, name='my_games'), 
    path("my-games/<int:page>", views.my_games, name = "my_games_paginate"),  
]