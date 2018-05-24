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
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, db_index=True, help_text='نام انگلیسی برای استفاده در لینک این دسته بندی')

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Post(models.Model):
    """
    Model for Posts
    """
    author=models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='نویسنده')
    title = models.CharField(max_length=100, unique=True, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, help_text='نام انگلیسی برای استفاده در لینک این نوشته')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    description = models.TextField(verbose_name='متن معرفی', help_text='توضیحات مختصری درباره‌ی این نوشته')
    content = RichTextUploadingField(config_name='awesome_ckeditor', verbose_name='متن اصلی', help_text='این متن در صفحه اصلی نوشته نمایش داده می‌شود')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    tags = TagField(verbose_name='برچسب‌ها', help_text='با استفاده از کاما (,) آنها را از یکدیگر جدا نمایید')

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    class Meta:
        verbose_name = 'نوشته'
        verbose_name_plural = 'نوشته ها'

class Comment(models.Model):
    """
    Model for Comments for Posts.
    """
    post=models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='نوشته')
    name=models.CharField(max_length=100, verbose_name='نام شما')
    email=models.EmailField(verbose_name='آدرس ایمیل')
    text=models.TextField(verbose_name='متن دیدگاه')
    date=models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')

    def __str__(self):
        return "{} --- {}".format(self.post.title, self.text)

    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه ها'

class Page(models.Model):
    """
    Model for make other page
    """
    title = models.CharField(max_length=100, unique=True, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, help_text='نام انگلیسی برای استفاده در لینک این برگه')
    content = RichTextUploadingField(config_name='awesome_ckeditor', verbose_name='محتوا')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_other_page', None, { 'slug': self.slug })
    
    class Meta:
        verbose_name = 'برگه'
        verbose_name_plural = 'برگه‌ها'