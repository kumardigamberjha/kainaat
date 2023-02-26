from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.name