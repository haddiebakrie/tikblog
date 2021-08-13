from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.
class PostCategoryTable(admin.TabularInline):
    model = Comment

class CategoryPostTable(admin.TabularInline):
    model = Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'status')
    list_filter = ('status',)
    search_field = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostCategoryTable]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'date_added')
    list_filter = ('date_added',)
    search_field = ('user', 'body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CategoryPostTable]


