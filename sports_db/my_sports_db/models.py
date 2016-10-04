from django.db import models

class Fighter(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    fights = models.IntegerField()
    strikes = models.IntegerField()
    strike_accuracy = models.FloatField()
    takedowns = models.IntegerField()
    takedown_accuracy = models.FloatField()
    knockdowns = models.IntegerField()
    passes = models.IntegerField()
    reversals = models.IntegerField()
    submissions = models.IntegerField()
