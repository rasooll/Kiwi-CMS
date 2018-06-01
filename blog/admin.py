from django.contrib import admin
from blog.models import Post, Category, Comment, Page, GeneralSetting, Navbar

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'published_date', 'category', 'tags')
    list_filter = ('published_date','category',)
    search_fields = ('title', 'slug', 'tags')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')

def make_accepted(modeladmin, request, queryset):
    queryset.update(accepted=True)
make_accepted.short_description = "تایید دیدگاه‌های انتخاب شده"

def make_unaccepted(modeladmin, request, queryset):
    queryset.update(accepted=False)
make_unaccepted.short_description = "عدم تایید دیدگاه‌های انتخاب شده"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'text', 'accepted', 'date')
    #list_editable = ('accepted',)
    list_filter = ('date','accepted',)
    search_fields = ('text', 'post')
    raw_id_fields = ('post',)
    actions = (make_accepted,make_unaccepted,)

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'published_date')

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