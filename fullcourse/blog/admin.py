from django.contrib import admin
from .models import Article, Category

# --- admin header change
admin.site.site_header = "وبلاگ"

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status = 'p')
    if rows_updated == 1:
        message_bit = 'منتشر شد'
    else:
        message_bit ='منتشر شدند'
    modeladmin.message_user(request, '{} مقاله {} ' .format(rows_updated, message_bit))        
make_published.short_description = 'انتشار مقالات انتخاب شده'    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','status', 'parent')
    list_filter =(['status'])
    search_fields =('title','slug')
    # --- auto fill slug field 
    prepopulated_fields = {'slug':('title',)}
    # --- order records in panel admin '-' means nozoli
admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag','created','author', 'jpublish','category_to_str','status')
    list_filter =('publish','author','title','status')
    search_fields =('title','description')
    # --- auto fill slug field 
    prepopulated_fields = {'slug':('title',)}
    # --- order records in panel admin '-' means nozoli
    ordering = ['-status','-publish']
    actions = [make_published]

    def category_to_str(self,obj):
        return ",".join([category.title for category in obj.category.active()])
    category_to_str.short_description = "دسته بندی"    

admin.site.register(Article,ArticleAdmin)
