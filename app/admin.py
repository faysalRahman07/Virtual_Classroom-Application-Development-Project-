from django.contrib import admin
from .models import Post, Comment, Category


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'user']
    search_fields = ['title']
    list_filter = ['user', 'created_at']
    list_per_page = 20
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'created_at']
    search_fields = ['text']
    list_per_page = 20
    date_hierarchy = 'created_at'
