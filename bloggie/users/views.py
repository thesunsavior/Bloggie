from distutils.log import info
from pickle import TRUE
from unicodedata import name
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import FB_User, GG_User
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FacebookAuthForm, GoogleAuthForm
from django.contrib.auth.decorators import login_required
from blog.models import Post


def sign_in_processor(request):
    user = request.user
    required = []
    # for f in required:
    #     if not f:
    return redirect('profile_edit')

    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Acount created for {username}!")
            return redirect('login')
    else:
        form = UserRegisterForm
    return render(request, 'users/register.html', {'form': form})


def redirect_resolve(request):
    if not request.user.is_authenticated:
        return redirect('blog-home')

    # if facebook
    social_account = FB_User.objects.filter(user=request.user).first()
    print(social_account)
    if (social_account != None):
        if (social_account.info == False):
            form = FacebookAuthForm(request.POST)
            if (form.is_valid()):
                name = form.cleaned_data.get('name')
                phoneNumber = form.cleaned_data.get('phoneNumber')

                social_account.name = name
                social_account.phoneNumber = phoneNumber
                social_account.info = True
                return redirect('blog-home')

            return render(request, 'socialaccount/fb-register.html',
                          {'form': form})

    #if google
    social_account = GG_User.objects.filter(user=request.user).first()
    print(social_account)
    if (social_account != None):
        if (social_account.info == False):
            form = GoogleAuthForm(request.POST)
            if (form.is_valid()):
                name = form.cleaned_data.get('name')
                occupation = form.cleaned_data.get('occupation')

                social_account.name = name
                social_account.occupation = occupation
                social_account.info = True
                social_account.save()
                return redirect('blog-home')

            return render(request, 'socialaccount/gg-register.html',
                          {'form': form})

    #if none social login
    return redirect('blog-home')


@login_required
def profile(request):

    posts = Post.objects.filter(author=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form, 'posts': posts}

    return render(request, 'users/profile.html', context)
