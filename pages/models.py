from django.db import models


class Company(models.Model):
    name = models.CharField(blank=True, max_length=300)
    ticker = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return f"({self.ticker}) {self.name}"