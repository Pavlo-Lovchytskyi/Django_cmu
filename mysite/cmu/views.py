from django.shortcuts import render
from django.http import HttpResponse

from users.models import Profile

def main(request):
    return render(request, 'cmu/main.html')


def index(request):
    photo = Profile.objects.all()
    img = {'photo': photo}
    return render(request, 'cmu/index.html', img)
