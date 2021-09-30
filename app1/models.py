from django.db import models
from django.contrib.auth.models import User
class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(null=True)
    tag = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.title + ', ' + self.tag

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)