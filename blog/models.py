from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Blog(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TagField()

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
