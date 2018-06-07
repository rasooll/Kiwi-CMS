from django.contrib import admin
from blog.models import Post, Category, Comment, Page, GeneralSetting, Navbar
from django_jalali.admin.filters import JDateFieldListFilter
#you need import this for adding jalali calander widget
import django_jalali.admin as jadmin

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'get_date', 'category', 'tags')
    list_filter = (('published_date', JDateFieldListFilter),'category',)
    search_fields = ('title', 'slug', 'tags')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')



class CommentAdmin(admin.ModelAdmin):
    def make_accepted(modeladmin, request, queryset):
        queryset.update(accepted=True)
    make_accepted.short_description = "تایید دیدگاه‌های انتخاب شده"

    def make_unaccepted(modeladmin, request, queryset):
        queryset.update(accepted=False)
    make_unaccepted.short_description = "عدم تایید دیدگاه‌های انتخاب شده"
    list_display = ('name', 'post', 'text', 'accepted', 'get_date')
    #list_editable = ('accepted',)
    list_filter = (('date', JDateFieldListFilter),'accepted')
    search_fields = ('text', 'post')
    #raw_id_fields = ('post',)
    actions = (make_accepted,make_unaccepted,)
    fields = ('accepted', 'post', 'name', 'email','text',)
    readonly_fields = ('post', 'name', 'email', 'text',)

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'get_date')

class GeneralSettingAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True

class NavbarAdmin(admin.ModelAdmin):
    list_display = ('title', 'ordering',)
    list_editable = ('ordering',)

admin.site.register(Post, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(GeneralSetting, GeneralSettingAdmin)
admin.site.register(Navbar, NavbarAdmin)