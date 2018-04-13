from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=300)
    achieved_at = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

    def pretty_date(self):
        return self.achieved_at.strftime("%b, %Y")
