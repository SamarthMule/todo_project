from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'completed', 'created_at')
    list_filter = ('completed', 'user')
    search_fields = ('title',)