from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from online_library.accounts.forms import CreateUserForm
from online_library.accounts.utils import get_full_name

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LogInUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    model = UserModel


class LogOutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class DetailsUserView(views.DetailView):
    template_name = 'accounts/details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fullname'] = get_full_name(self.request.user)
        return context


class EditUserView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/edit.html'
    model = UserModel
    fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class DeleteUserView(views.DeleteView):
    template_name = 'accounts/delete.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def post(self, *args, **kwargs):
        response = super().post(*args, **kwargs)

        return response
