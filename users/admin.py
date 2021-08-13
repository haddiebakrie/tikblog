from django.contrib import admin
from . models import Profile

# Register your models here.

@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('website',)