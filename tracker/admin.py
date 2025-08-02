from django.contrib import admin
from .models import Project, Bug, Comment

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display    = ['name', 'id', 'description', 'owner', 'created_at', 'updated_at']
    list_filter     = ['name', 'owner__username']
    search_fields   = ['name', 'owner__username']

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display    = ['title', 'id', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_by', 'created_at', 'updated_at']
    list_filter     = ['title', 'assigned_to__username', 'project__name', 'created_by__username']
    search_fields   = ['title', 'assigned_to__username', 'project__name', 'created_by__username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display    = ['bug', 'id', 'commenter', 'message', 'created_at', 'updated_at']
    list_filter     = ['bug__title', 'commenter__username']
    search_fields   = ['bug__title', 'commenter__username']