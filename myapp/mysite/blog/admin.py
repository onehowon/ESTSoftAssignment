from django.contrib import admin
from .models import Post, Category, Tag, Comment

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slugs':('name',)}
    
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)


# Register your models here.
