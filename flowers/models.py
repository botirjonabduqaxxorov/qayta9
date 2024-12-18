from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='flowers')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
