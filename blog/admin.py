from django.contrib import admin

from .models import Author, Post, Tag, Comment
# Register your models here.
 
class AuthorAdmin(admin.ModelAdmin):
    pass
    # list_display = ('first_name', 'last_name')

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'slug', 'date')
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("tag", "author", "date")

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)