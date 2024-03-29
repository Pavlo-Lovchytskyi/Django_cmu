from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Game, Genre

@login_required
def main(request, page=1):
    games = Game.objects.all()
    genres = Genre.objects.all()
    per_page = 6
    paginator = Paginator(list(games), per_page)
    games_on_page = paginator.page(page)
    return render(request, 'games/games.html', context={'games':games_on_page, 'genres': genres})

@login_required
def my_games(request, page=1):
    if request.user.is_authenticated:
        user_games = request.user.profile.game.all()
    else:
        user_games = None
    
    games = Game.objects.all()
    genres = Genre.objects.all()
    per_page = 6
    paginator = Paginator(list(games), per_page)
    games_on_page = paginator.page(page)
    
    return render(request, 'games/my_games.html', context={'games': games_on_page, 'genres': genres, 'user_games': user_games})


@login_required
def game_detail(request, game_name):
    game = get_object_or_404(Game, name=game_name)
    user = request.user
    is_purchased = user.profile.game.filter(name=game_name).exists()
    return render(request, 'games/game_detail.html', {'game_detail': game, 'is_purchased': is_purchased})


@login_required
def my_game_detail(request, game_name):
    game = get_object_or_404(Game, name=game_name)
    return render(request, 'games/my_game_detail.html', {'game_detail': game})


@login_required
def buy_game(request, game_name):
    game = get_object_or_404(Game, name=game_name)
    if request.user.profile.game.filter(name=game_name).exists():
        messages.error(request, 'You already own this game.')
    else:
        request.user.profile.game.add(game)
        messages.success(request, f'You have successfully bought {game_name}.')
    return redirect('games:game_detail', game_name=game_name)

