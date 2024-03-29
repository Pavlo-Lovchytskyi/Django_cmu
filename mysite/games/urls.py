from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.main, name='main'), 
    path("main/<int:page>", views.main, name = "main_paginate"),
    path('my-games/', views.my_games, name='my_games'), 
    path("my-games/<int:page>", views.my_games, name = "my_games_paginate"), 
    path("<str:game_name>/", views.game_detail, name="game_detail"),
    path("my-games/<str:game_name>/", views.my_game_detail, name="game_detail"), 
    path('<str:game_name>/buy/', views.buy_game, name='buy_game'), 
]