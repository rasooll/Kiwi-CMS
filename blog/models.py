from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    """
    Model for Category
    """
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Post(models.Model):
    """
    Model for Posts
    """
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    content = RichTextUploadingField(config_name='awesome_ckeditor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TagField()

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Comment(models.Model):
    """
    Model for Comments for Posts.
    """
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} --- {}".format(self.post.title, self.text)