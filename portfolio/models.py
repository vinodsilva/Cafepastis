from django.db import models

class Images(models.Model):
    alt = models.CharField(max_length=60)
    link = models.CharField(max_length=400, default=None,blank=True, null=True)
    image = models.ImageField(upload_to="",  default=None,blank=True, null=True)

    def __str__(self):
        return self.alt
