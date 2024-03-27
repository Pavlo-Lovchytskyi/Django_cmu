from django.http import HttpResponseForbidden
from django.contrib.auth import logout
from .models import Profile

class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                if profile.is_banned:
                    return HttpResponseForbidden("Ты забанен, ЧМОШНИК.")
            except Profile.DoesNotExist:
                pass
        return None
