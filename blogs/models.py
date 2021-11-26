from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.post.title

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'pk':self.pk})

class Event(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='profile_pics')
    details = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('events_detail',
                    kwargs={'pk':self.pk})