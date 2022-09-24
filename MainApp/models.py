from django.db import models



class CsvData(models.Model):
    banknifty = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(default=True)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.time
