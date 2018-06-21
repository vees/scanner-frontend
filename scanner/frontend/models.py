from django.db import models

# Create your models here.
class Transmission(models.Model):
    recordtime = models.DateTimeField()
    sequence = models.SmallIntegerField()
    transcript = models.TextField()
    confidence = models.DecimalField(max_digits=4, decimal_places=3)
