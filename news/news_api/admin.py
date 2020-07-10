from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("title", "author")
    list_display = ("title", "author", "creation_date")


admin.site.register(Comment)
