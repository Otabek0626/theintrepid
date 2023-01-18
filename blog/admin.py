from django.contrib import admin
from .models import Post, Tag

class TagInline(admin.TabularInline):
    model = Post.tags.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TagInline]
    
admin.site.register(Tag)