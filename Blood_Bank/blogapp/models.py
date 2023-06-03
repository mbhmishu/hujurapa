from django.db import models
from AccountApp.models import User
# Create your models here.



# Create your models here.
class Blog(models.Model):
    author=models.ForeignKey(User, related_name='blog_content', on_delete=models.CASCADE)
    title=models.CharField(max_length=200, verbose_name='Blog Title' )
    slug = models.SlugField(max_length=300, unique=True)
    blog_content = models.TextField(verbose_name='Whats your mind?' )
    blog_img=models.ImageField(upload_to='BlogImg', verbose_name='Image', blank=True)
    creat_date=models.DateTimeField(auto_now_add=True)
    edit_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-creat_date',)

    def __str__(self):
        return self.title



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment=models.TextField()
    comment_date=models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date',]
    
    def __str__(self):
        return self.comment


class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='like_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')

    def __str__(self):
        return self.user + 'likes' + self.blog


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    date = models.DateTimeField(auto_now_add=True)



