from django.contrib import admin
from .models import ActivityLog

# Register your models here.
@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display    = ['project', 'user', 'action', 'ip_address', 'created_at']
    list_filter     = ['project', 'action', 'user']
    search_fields   = ['project__name', 'user__username', 'action', 'ip_address', 'description']
    readonly_fields = ['project', 'user', 'action', 'ip_address', 'description', 'data', 'created_at']