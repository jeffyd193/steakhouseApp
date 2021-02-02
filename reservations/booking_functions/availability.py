import datetime
from reservations.models import Table, Reservations


def check_availability(table, check_in, check_out):
    table_list=[]
    reservations_list = Reservations.objects.filter(table=table)
    for reservations in reservations_list:
        if reservations.check_in > check_out or reservations.check_out < check_in:
            table_list.append(True)
        else:
            table_list.append(False)
    return all(table_list)

"""
check availability
make a list to store
filter in tables as objects
loop over the list
if check_in time + 1 hour > or c
"""