from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Game, Genre


def main(request, page=1):
    games = Game.objects.all()
    genres = Genre.objects.all()
    per_page = 2
    paginator = Paginator(list(games), per_page)
    games_on_page = paginator.page(page)
    return render(request, 'games/games.html', context={'games':games_on_page, 'genres': genres})

