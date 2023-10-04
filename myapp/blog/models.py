from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_regular_member = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Post(models.Model):
    title = models.CharField(verbose_name='글 제목', max_length=30)
    content = models.TextField(verbose_name='글 내용')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
