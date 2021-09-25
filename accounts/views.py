from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LogoutView


class MyLogoutView(LogoutView):
    next_page = None
    template_name = 'accounts/logged_out.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def get_to_user_profile(request) -> HttpResponse:
    if request.user.is_authenticated:
        print('ОК', f'Пользователь {request.user.get_username()}')
    else:
        print('NO')
    print(request.user.get_username())
    return render(request, template_name=f'accounts/profile.html',)
