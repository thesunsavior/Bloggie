from pickle import TRUE
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import FB_User, GG_User
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FacebookAuthForm, GoogleAuthForm
from django.contrib.auth.decorators import login_required


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


def ggReg(request):
    form = GoogleAuthForm
    return render(request, 'socialaccount/gg-register.html', {'form': form})


def fbReg(request):
    form = FacebookAuthForm
    return render(request, 'socialaccount/fb-register.html', {'form': form})


def redirect_resolve(request):
    # if facebook
    social_account = FB_User.objects.filter(user=request.user).first()
    print(social_account)
    if (social_account != None):
        if (social_account.info == False):
            form = FacebookAuthForm(request.POST)
            if (form.is_valid()):
                form.save()
                social_account.update(info=True)
                return redirect('home')

            return render(request, 'socialaccount/fb-register.html',
                          {'form': form})

    #if google
    social_account = GG_User.objects.filter(user=request.user).first()
    print(social_account)
    if (social_account != None):
        if (social_account.info == False):
            form = GoogleAuthForm(request.POST)
            if (form.is_valid()):
                form.save()
                social_account.update(info=True)
                return redirect('home')

            return render(request, 'socialaccount/gg-register.html',
                          {'form': form})

    #if none social login
    return redirect('home')


@login_required
def profile(request):

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

    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'users/profile.html', context)
