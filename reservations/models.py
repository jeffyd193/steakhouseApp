from django.db import models
from django.conf import settings
from datetime import datetime, timedelta

# Create your models here.

class Table(models.Model):
    TABLE_CATEGORIES =(
        ('Window', 'Window'),
        ('Booth', 'Booth'),
        ('Table', 'Table'),
        ('Events', 'Events')
    )
    category = models.CharField(max_length=6, choices=TABLE_CATEGORIES, default='Select')
    section = models.IntegerField(default=0)
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'Section {self.section}, Table {self.number}: {self.category} Table. Seats {self.capacity} People'

class Reservations(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        self.check_out = self.check_in + timedelta(hours=1)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} checks in table #{self.table} from {self.check_in} to {self.check_out}'