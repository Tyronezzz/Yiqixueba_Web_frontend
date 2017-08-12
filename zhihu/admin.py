from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import User, Article, Tag

# Register your models here.


    # Re-registration UserAdmin
#admin.site.registration(User)

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article)
