from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'date_joined')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display    = ['username', 'id' , 'email', 'is_superuser', 'is_staff', 'date_joined', 'last_login', 'is_active']
    search_fields   = ('email', 'username')
    ordering        = ('-date_joined',)

# Unregister User from default admin site
admin.site.unregister(User)

# Register Custom user admin
admin.site.register(User, UserAdmin)