from django.db import models


# Create your models here.
class PublishedModel(models.Model):
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
