from django.contrib import admin
from .models import Category,Comment,Post,Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','slug', 'title', 'category', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', )
    readonly_fields = ('created_at',)
    prepopulated_fields = ({'slug':('title',)})


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_filter = ('created_at', )
    readonly_fields = list_filter
    search_fields = ('name', 'email',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)