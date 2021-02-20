from django.db import models
from django.contrib.auth.models import User
from .snippets import generate_unique_slug, choices
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_posts")
    title = models.CharField(max_length=120)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_posts")
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    attachment = models.FileField(upload_to="videos/", blank=True, null=True)
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    views = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:100]
