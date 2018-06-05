from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField
from ckeditor_uploader.fields import RichTextUploadingField
from django_jalali.db import models as jmodels

# Create your models here.

class Category(models.Model):
    """
    Model for Category
    """
    title = models.CharField(
        max_length=100,
        verbose_name='عنوان'
    )
    slug = models.SlugField(
        max_length=100,
        db_index=True,
        help_text='نام انگلیسی برای استفاده در لینک این دسته بندی'
    )

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
    author=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='نویسنده'
    )
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='عنوان'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text='نام انگلیسی برای استفاده در لینک این نوشته'
    )
    published_date = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name='زمان انتشار'
    )
    modified_date = jmodels.jDateTimeField(
        auto_now=True,
        verbose_name='زمان ویرایش'
    )
    description = models.TextField(
        verbose_name='متن معرفی',
        help_text='توضیحات مختصری درباره‌ی این نوشته'
    )
    content = RichTextUploadingField(
        config_name='awesome_ckeditor',
        verbose_name='متن اصلی',
        help_text='این متن در صفحه اصلی نوشته نمایش داده می‌شود'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='دسته بندی'
    )
    tags = TagField(
        verbose_name='برچسب‌ها',
        help_text='با استفاده از کاما (,) آنها را از یکدیگر جدا نمایید'
    )

    def __str__(self):
        return self.title

    def get_date(self):
        return self.published_date.strftime("%d %B %Y %H:%M")
    get_date.short_description = 'زمان انتشار'

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    class Meta:
        verbose_name = 'نوشته'
        verbose_name_plural = 'نوشته ها'
        ordering = ['published_date']

class Comment(models.Model):
    """
    Model for Comments for Posts.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='نوشته'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='نام شما'
    )
    email = models.EmailField(
        verbose_name='آدرس ایمیل'
    )
    text = models.TextField(
        verbose_name='متن دیدگاه'
    )
    date = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name='زمان انتشار'
    )
    accepted = models.BooleanField(
        default=False,
        verbose_name='تایید شده؟'
    ) 

    def get_date(self):
        return self.date.strftime("%d %B %Y %H:%M")
    get_date.short_description = 'زمان انتشار'

    def __str__(self):
        return "{} --- {}".format(self.post.title, self.name)

    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه ها'

class Page(models.Model):
    """
    Model for make other page
    """
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='عنوان'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text='نام انگلیسی برای استفاده در لینک این برگه'
    )
    content = RichTextUploadingField(
        config_name='awesome_ckeditor',
        verbose_name='محتوا'
    )
    published_date = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name='زمان انتشار'
    )

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_other_page', None, { 'slug': self.slug })
    
    class Meta:
        verbose_name = 'برگه'
        verbose_name_plural = 'برگه‌ها'
    
class GeneralSetting(models.Model):
    """
    Model for general blog setting
    """
    Title = models.CharField(
        verbose_name='عنوان سایت',
        max_length=150,
        db_index=True
    )
    Description = models.CharField(
        verbose_name='توضیحات سایت',
        max_length=300,
        blank=True,
        null=True,
        db_index=True
    )
    Footer = models.CharField(
        verbose_name='متن فوتر',
        max_length=400,
        blank=True,
        null=True,
        db_index=True
    )
    DateTypeValue=(
        ('IR', 'جلالی'),
        ('EN', 'میلادی'),
    )
    DateType = models.CharField(
        verbose_name='نوع نمایش تاریخ در سایت',
        max_length=2,
        choices=DateTypeValue,
        default='IR'
    )
    PostNumber = models.PositiveSmallIntegerField(
        verbose_name='تعداد مطالب قابل نمایش در صفحه اصلی',
        default=10
    )
    CommentsDisable = models.BooleanField(
        verbose_name='غیرفعالسازی ارسال دیدگاه',
        default=False
    )
    SiteClose = models.BooleanField(
        verbose_name='سایت در دست تعمیر؟',
        default=False
    )

    class Meta:
        verbose_name = 'تنظیمات عمومی'
        verbose_name_plural = 'تنظیمات عمومی'

class Navbar(models.Model):
    """
    This model use for navbar item.
    """
    title = models.CharField(verbose_name='عنوان', max_length=60)
    page = models.ForeignKey(Page, verbose_name='برگه', on_delete=models.CASCADE)
    ordering = models.PositiveSmallIntegerField(verbose_name='چیدمان', default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'آیتم'
        verbose_name_plural = 'فهرست'
        ordering = ['ordering']
