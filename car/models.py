from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    engine = models.FloatField(default=0)
    power = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    cost = models.FloatField(default=0)

    class Meta:
        verbose_name = 'samochody'
        verbose_name_plural = "Samochody"

    def __str__(self):
        return self.make
