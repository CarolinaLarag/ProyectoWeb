from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(default='')
    image = models.ImageField(upload_to= 'blog', default='blog/static/images/no-img.jpg')
    price = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Proveedor(models.Model):
    name = models.TextField()
    text = models.TextField(default='')
    image = models.ImageField(upload_to= 'blog', default='blog/static/images/no-img.jpg')
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name   