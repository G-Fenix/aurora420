from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content')
