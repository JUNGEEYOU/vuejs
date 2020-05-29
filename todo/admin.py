from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed']  # 목록을 확인

admin.site.register(Todo, TodoAdmin)
