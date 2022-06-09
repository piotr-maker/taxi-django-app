from django.conf import settings
from django.db import models


class Locations(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.DecimalField(max_digits=9, decimal_places=6)


class Orders(models.Model):
    STATUS_CHOICES = [
        ('NE', 'New'),
        ('PR', 'In progress'),
        ('CA', 'Cancelled'),
        ('CL', 'Closed'),
    ]

    passenger = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE)
    driver = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE, null=True)
    order_from = models.ForeignKey(Locations, related_name='+', on_delete=models.CASCADE)
    order_to = models.ForeignKey(Locations, related_name='+', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NE')
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
