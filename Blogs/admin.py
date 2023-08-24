from django.contrib import admin
from .models import *
# Register your models here.


# for configration of category admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'content', 'posted_date')
    search_fields= ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display=('image_tag', 'title','posted_date')
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page= 50
class popularAdmin(admin.ModelAdmin):
    list_display=('image_tag', 'title','posted_date')
    search_fields=('title',)
    

admin.site.register(ContactUsTb)
admin.site.register(Popular_Blogs,popularAdmin)
admin.site.register(Regular_Blog,PostAdmin)
admin.site.register(Category, CategoryAdmin)
