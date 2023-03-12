from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Id {self.id}: {self.name}'
