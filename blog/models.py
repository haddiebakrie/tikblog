from django.db import models
from django.contrib.auth.models import User
import readtime

# Create your models here.

STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(default='No Description')
    image = models.ImageField(upload_to='uploads', blank=True)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Post(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text

    class Meta:
        ordering = ['-created_on']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    
    class Meta:
        ordering = ['date_added']
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return 'Comment {} made by {}'.format(self.body, self.user.username)

