import random
import secrets
import string

from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView, DeleteView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterFrom, UserProfileFrom
from users.models import User


class UserView(ListView):
    model = User
    fields = ['email', 'first_name', 'last_name', 'comment']
    template_name = 'users/user_list.html'
    extra_context = {'title': 'Пользователи'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserDDetailView(DetailView):
    model = User
    fields = ['email', 'first_name', 'last_name', 'comment']
    template_name = 'users/user_detail.html'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserCreateView(CreateView):
    model = User
    fields = ['email', 'first_name', 'last_name', 'comment']
    template_name = 'users/user_from.html'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание пользователя'
        return context


class UserUpdateView(UpdateView):
    model = User
    fields = ['email', 'first_name', 'last_name', 'comment']
    template_name = 'users/user_from.html'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_item = self.get_object()
        context['title'] = user_item.email
        return context


class UserLogin(LoginView):
    template_name = 'users/login.html'


class UserLogout(LogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterFrom
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.set_password(user.password)
        verification_code = secrets.token_hex(16)
        user.verification_code = verification_code
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{verification_code}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет, переди по ссылке для подтверждения почты {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        user.save()
        return super().form_valid(form)


def email_verification(request, verification_code):
    verification_code = request.POST.get('verification_code')
    user = get_object_or_404(User, verification_code=verification_code)
    if user:
        user.is_active = True
        user.save()
        return redirect(reverse("users:login"))
    else:
        return redirect(reverse('users:register'))


class ResetPassword(TemplateView):
    def get(self, request):
        return render(request, 'users/reset.html')

    def post(self, request):
        mail = request.POST.get('mail')
        user = get_object_or_404(User, email=mail)
        letters = list(string.ascii_lowercase)
        new_password = ''
        for i in range(8):
            new_password = new_password + random.choice(letters) + str(random.randint(1, 9))
            user.set_password(new_password)
        user.save()
        message = (f'Ваш новый пароль: {new_password}'
                   f'Сохраняйте в тайне!')
        send_mail(
            subject='Новый пароль',
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return redirect('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileFrom
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
