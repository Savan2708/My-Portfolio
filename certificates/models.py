from django.db import models


# Create your models here.


class Certificates(models.Model):
    img = models.ImageField(upload_to='imges/')
    title = models.CharField(max_length=255, null=True)
    body = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title

    def formated_date(self):
        return self.date.strftime('%b %e %Y')