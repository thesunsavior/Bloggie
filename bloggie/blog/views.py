from http.client import HTTPResponse
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
# Create your views here.

#some dummy data to load some post
# posts = [
#     {
#         'author': 'dickie',
#         'title': 'my dickie dickie',
#         'content': 'my dickie grew',
#         'date_posted': 'june 15,2022'
#     },
#     {
#         'author': 'Johny deep',
#         'title': 'the starlight of my life',
#         'content': 'starlight sucked me ',
#         'date_posted': 'june 12,2021'
#     },
# ]


def home(request):
    context = {'posts': Post.objects.all}

    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.author):
            return True

        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.author):
            return True

        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})


class AddLike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        all_like = Post.objects.get(pk=pk)

        already_Like = False
        for i in all_like.likes.all():
            if (i == request.user):
                already_Like = True
                break

        if already_Like:
            all_like.likes.remove(request.user)
        else:
            all_like.likes.add(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)
