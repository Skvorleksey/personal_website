from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime
from .forms import PostUpdateForm


class PostsListView(ListView):
    model = BlogPost
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    queryset = BlogPost.objects.order_by('-publication_date_time')


class PostsDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_details.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ('text',)
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog:posts')

    def form_valid(self, form):
        form.instance.publication_date_time = datetime.now()
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = BlogPost
    # fields = ('text',)
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog:posts')
    form_class = PostUpdateForm

    def form_valid(self, form):
        form.instance.edited = True
        form.instance.edited_date_time = datetime.now()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
