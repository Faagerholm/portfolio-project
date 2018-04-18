from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=400)
    time = models.DateTimeField(default=timezone.now)

    def pub_date_short(self):
        return self.time.strftime('%b %e %Y')
