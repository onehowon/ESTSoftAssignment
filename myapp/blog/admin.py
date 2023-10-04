from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('email', 'name', 'is_regular_member', 'created_at', 'updated_at',)
    list_editable = ('is_regular_member',)
    search_fields = ('name',)
    
admin.site.register(User, UserAdmin)

# Register your models here.
