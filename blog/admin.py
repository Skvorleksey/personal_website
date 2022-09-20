from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'publication_date_time',
        'text',
    )


admin.site.register(BlogPost, BlogPostAdmin)
