# Generated by Django 3.1.6 on 2021-02-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_table_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='check_out',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]