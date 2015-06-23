from django.contrib import admin

from .models import Category, Post, Announcement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Announcement)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
