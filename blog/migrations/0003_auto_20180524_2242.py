# Generated by Django 2.0.5 on 2018-05-24 18:12

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان')),
                ('slug', models.SlugField(help_text='نام انگلیسی برای استفاده در لینک این برگه', max_length=100, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
            ],
            options={
                'verbose_name': 'برگه',
                'verbose_name_plural': 'برگه\u200cها',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'دیدگاه', 'verbose_name_plural': 'دیدگاه ها'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'نوشته', 'verbose_name_plural': 'نوشته ها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='نام انگلیسی برای استفاده در لینک این دسته بندی', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='آدرس ایمیل'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام شما'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='نوشته'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='متن دیدگاه'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='این متن در صفحه اصلی نوشته نمایش داده می\u200cشود', verbose_name='متن اصلی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(help_text='توضیحات مختصری درباره\u200cی این نوشته', verbose_name='متن معرفی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='نام انگلیسی برای استفاده در لینک این نوشته', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=tagging.fields.TagField(blank=True, help_text='با استفاده از کاما (,) آنها را از یکدیگر جدا نمایید', max_length=255, verbose_name='برچسب\u200cها'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='عنوان'),
        ),
    ]