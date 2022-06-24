from django.contrib import admin
from .models import FB_User, GG_User, Profile

admin.site.register(Profile)
admin.site.register(FB_User)
admin.site.register(GG_User)
