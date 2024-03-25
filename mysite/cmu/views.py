from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from users.models import Profile

def main(request):
    return render(request, 'cmu/main.html')


def index(request):
    #profile = Profile.objects.all()
    profile = Profile.objects.get(user=request.user)
    age = (datetime.now().date() - profile.birthday).days // 365
    profile = {'profile': profile, 'age': age}
    return render(request, 'cmu/index.html', profile)
