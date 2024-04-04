from django.contrib import admin
from .models import CustomUser, Todo

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', "last_login"]
    search_fields = ['email']
    

class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'updated_at', 'created_at']
    search_fields = ['task']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Todo, TodoAdmin)