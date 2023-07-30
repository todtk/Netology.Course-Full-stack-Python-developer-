from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        verbose_name='measurement',
        related_name='measurements',
    )
    image = models.ImageField(null=True)
