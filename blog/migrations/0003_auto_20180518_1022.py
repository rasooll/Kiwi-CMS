# Generated by Django 2.0.5 on 2018-05-18 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tag',
            new_name='tags',
        ),
    ]
