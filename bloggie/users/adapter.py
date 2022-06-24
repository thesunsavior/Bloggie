from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import FB_User, GG_User
from .form import GoogleAuthForm, FacebookAuthForm
from allauth.account.adapter import get_adapter as get_account_adapter
from django.shortcuts import redirect


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    # def get_connect_redirect_url(self, request, socialaccount):
    #     """
    #     Returns the default URL to redirect to after successfully
    #     connecting a social account.
    #     """
    #     print(
    #         "******************************* REDIRECT************************************"
    #     )
    #     assert request.user.is_authenticated
    #     if socialaccount.provider == 'Facebook':
    #         url = reverse("fb-register")
    #     else:
    #         url = reverse("gg-register")
    #     return url

    def save_user(self, request, sociallogin, form=None):
        """
        Saves a newly signed up social login. In case of auto-signup,
        the signup form is not available.
        """
        u = sociallogin.user
        u.set_unusable_password()
        if form:
            get_account_adapter().save_user(request, u, form)
        else:
            get_account_adapter().populate_username(request, u)

        sociallogin.save(request)

        print("************Redirect nowww *******************")
        if (sociallogin.account.provider == 'facebook'):
            temp = FB_User.objects.create(user=sociallogin.user)
            temp.save()
        else:
            temp = GG_User.objects.create(user=sociallogin.user)
            temp.save()
        return u


# settings.py
# SOCIALACCOUNT_ADAPTER = "point.to.adaptor.SocialAccountAdapter"