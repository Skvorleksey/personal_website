from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import User
from blog.models import BlogPost


class CreateUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('main:index')


class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/update_user.html'
    success_url = reverse_lazy('main:index')
    # form_class = UserChangeForm
    fields = ('username', 'hobby', 'company', 'photo')

    def get_object(self, queryset=None):
        return self.request.user


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.filter(author=context['user'])
        return context
