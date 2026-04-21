from django.db import models
from django.contrib.auth.models import User

class Customers(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    document_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=250)

class Appointments(models.Model):
    APPOINTMENT_STATUS = (
        ('PENDING', 'PENDING'),
        ('FINISHED', 'FINISHED'),
        ('CANCELLED', 'CANCELLED'),
    )
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(
        Customers,
        on_delete=models.CASCADE,
        db_column='customer_id',
        related_name='appointments'
    )
    service = models.ForeignKey(
        'services.Services',
        on_delete=models.CASCADE,
        db_column='service_id',
        related_name='appointments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='appointments'
    )
    barber = models.ForeignKey(
        'services.Barbers',
        on_delete=models.CASCADE,
        db_column='barber_id',
        related_name='appointments'
    )