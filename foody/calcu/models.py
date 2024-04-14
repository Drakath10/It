from django.db import models

# Create your models here.
class meal(models.Model):
    carbs=models.FloatField()
    protein=models.FloatField()
    calories=models.FloatField()