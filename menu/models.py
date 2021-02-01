from django.db import models
from django.conf import settings

# Create your models here.
class Food(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30, default='Name')
    price = models.IntegerField()
    description = models.CharField(max_length=300, default='Description')
    FOOD_CATEGORY = (
        ('Drink', 'Drink'),
        ('Dinner', 'Dinner'),
        ('Lunch', 'Lunch')
    )
    category = models.CharField(max_length=6, choices=FOOD_CATEGORY, default='choose')
    def __str__(self):
        return f'{self.name} was added to the {self.category} menu.'
