from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Game, Genre


def main(request, page=1):
    games = Game.objects.all()
    genres = Genre.objects.all()
    per_page = 21
    paginator = Paginator(list(games), per_page)
    games_on_page = paginator.page(page)
    return render(request, 'games/games.html', context={'games':games_on_page, 'genres': genres})


def my_games(request, page=1):
    if request.user.is_authenticated:
        user_games = request.user.profile.game.all()
    else:
        user_games = None
    
    games = Game.objects.all()
    genres = Genre.objects.all()
    per_page = 21
    paginator = Paginator(list(games), per_page)
    games_on_page = paginator.page(page)
    
    return render(request, 'games/my_games.html', context={'games': games_on_page, 'genres': genres, 'user_games': user_games})

