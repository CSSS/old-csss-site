from django.contrib import admin

from .models import Category, Post, Announcement
from django_markdown.admin import MarkdownModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(MarkdownModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Announcement)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
