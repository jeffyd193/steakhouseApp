from django.urls import path
from .views import TableListView, ReservationsList, TableDetailView, ReservationsView, TableListView

app_name = 'reservations'

urlpatterns = [
    path('table_list/', TableListView.as_view(), name='TableList'),
    path('reservation_list/', ReservationsList.as_view(), name='ReservationsList'),
    path('reservation/', ReservationsView.as_view(), name='ReservationsList'),
    path('table/<category>', TableDetailView.as_view(), name='TableDetail'),
]

