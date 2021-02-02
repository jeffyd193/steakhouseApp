from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from .models import Table, Reservations
from .forms import AvailabilityForm
from reservations.booking_functions.availability import check_availability
from datetime import datetime, timedelta

# Create your views here.

class TableListView(ListView):
    model=Table

class ReservationsList(ListView):
    model=Reservations

class TableDetailView(View):
    def get(self, request, *args, **kwargs):
        table_category = self.kwargs.get('category', None)
        table_list = Table.objects.filter(category=category)
        table = table_category[0]
        return render()
        



    def post(self, request, *args, **kwargs):
        table_list = Table.objects.filter(category=category)
        availability_tables=[]
        for table in table_list:
            if check_availability(table, data['check_in'], data['check_out']):
                availability_tables.append(table)
        if len(availability_tables)>0:
            table = availability_tables[0]
            reservations = Reservations.objects.create(
                user = self.request.user, 
                table = table,
                check_in = data['check_in'],
                check_out = data['check_out'],
            )
            reservations.save()
            return HttpResponse(reservations)
        else:
            return HttpResponse('This category of tables are booked. Try Another')

class ReservationsView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(category=data['table_category'])
        availability_tables=[]
        for table in table_list:
            if check_availability(table, data['check_in'], data['check_out']): #
                availability_tables.append(table)
        if len(availability_tables)>0:
            table = availability_tables[0]
            reservations = Reservations.objects.create(
                user = self.request.user, 
                table = table,
                check_in = data['check_in'],
                check_out = data['check_out'],
            )
            reservations.save()
            return HttpResponse(reservations)
        else:
            return HttpResponse('This category of tables are booked. Try Another')