from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
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


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
