from django.contrib import admin
from .models import Post,Comment,Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display =['title' ,'draft' ,'category']
    search_fields =['title']
    list_filter =['draft' ,'category']
    
admin.site.register(Post ,PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
