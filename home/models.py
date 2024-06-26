from django.db import models

# Create your models here.
class Update(models.Model):
    """ Updates on home screen """
    
    heading_update = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.heading_update}"
