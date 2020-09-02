from django.contrib import admin

from post.models import Post, Image


class ImageInline(admin.TabularInline):
    extra = 0
    model = Image


class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['id', 'timestamp', 'user', '_images']

    def _images(self, post) -> int:
        return post.images.count()


admin.site.register(Image)
admin.site.register(Post, PostAdmin)
