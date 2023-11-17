from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

'''
posts:
1-title
2-content
3-draft
4-public-date
4-img
-tags  --- using library tagit from django packages


5-category
6-comment
# Create your models here.'''
class Post(models.Model):
    author =models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content =models.TextField(max_length=20000)
    draft =models.BooleanField(default=True)
    public_dat_time =models.DateTimeField(default=timezone.now)
    image= models.ImageField(upload_to='posts', height_field=None, width_field=None, max_length=None)

    category = models.ForeignKey("Category", related_name='post_categry', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name =models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    user =models.CharField( max_length=50)
    content =models.TextField(max_length=500)
    date_of_publish =models.DateTimeField( default=timezone.now)

    post =models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    





