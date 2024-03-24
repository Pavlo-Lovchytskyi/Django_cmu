from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Game, Genre


def main(request):
    games = Game.objects.all()
    return render(request, 'games/games.html', context={'games':games})

