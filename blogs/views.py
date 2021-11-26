from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Event
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    paginate_by = 3

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def index(request):
    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html',{'title': 'About'})


class CreateComment(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ['post','name', 'content', 'date_created']
    template_name = 'add_comment.html'
    ordering = ['-date_created']


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'

class EventListView(ListView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'events'
    ordering = ['date']

class EventDetailView(DetailView):
    model = Event
    template_name = 'events_detail.html'

class EventCreateView(CreateView):
    model = Event
    template_name = 'events_form.html'
    fields = ['title', 'image', 'details']

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events_update.html'
    fields = fields = ['title', 'image', 'details']

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events_delete.html'
    success_url = '/'
