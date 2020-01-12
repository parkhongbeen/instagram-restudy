from django.contrib import admin

from posts.models import Post, PostImage, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostImage)
class PostImage(admin.ModelAdmin):
    pass


