from django.contrib import admin
from blog.models import Post, Category, Comment

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'published_date', 'category', 'tags')
    list_filter = ('published_date',)
    search_fields = ('title', 'slug', 'tags')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'text', 'date')
    list_filter = ('date',)
    search_fields = ('text', 'post')

admin.site.register(Post, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)