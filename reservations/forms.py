from .models import Reservations
from django import forms

class AvailabilityForm(forms.Form):
    TABLE_CATEGORIES =(
        ('Window', 'Window'),
        ('Booth', 'Booth'),
        ('Table', 'Table'),
        ('Events', 'Events')
    )
    table_category = forms.ChoiceField(choices=TABLE_CATEGORIES, required=True)
    guests = forms.IntegerField(required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = Reservations.check_out
