from django.contrib import admin
from api.models import Profile, Book


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'published_date', 'is_available', 'price']


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'rdoc']

