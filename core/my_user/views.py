from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from my_user.forms import RegisterForm


class SignUpView(CreateView):
    template_name = 'my_user/sign_up.html'
    form_class = RegisterForm
    success_url = reverse_lazy('log_in')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('start_page')

        return super().get(request, *args, **kwargs)


class UserLoginView(LoginView):
    template_name = 'my_user/log_in.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start_page')


class UserLogoutView(LogoutView):
    template_name = 'my_user/log_out.html'
    next_page = reverse_lazy('start_page')


def profile_view(request):
    user = request.user
    context = {'user': user}

    return render(request, 'my_user/profile.html', context)

