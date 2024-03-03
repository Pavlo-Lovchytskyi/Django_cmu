from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'cmu/main.html')


def index(request):
    return render(request, 'cmu/index.html')
