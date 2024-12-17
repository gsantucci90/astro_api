from django.db import models

class DataRelease(models.Model):
    name = models.CharField(max_length=100)
    pretty_name = models.CharField(max_length=100)
    version = models.FloatField()

    def __str__(self):
        return self.pretty_name

class AstronomicalObject(models.Model):
    right_ascension = models.FloatField()
    declination = models.FloatField()
    source_name = models.CharField(max_length=100)
    data_release = models.ForeignKey(DataRelease, on_delete=models.PROTECT)

        
    def __str__(self):
        return self.source_name
