from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    duration = models.IntegerField()

class Barbers(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    speciality = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class Schedules(models.Model):
    DAYS_OF_WEEK = (
        ('MONDAY', 'MONDAY'),
        ('TUESDAY', 'TUESDAY'),
        ('WEDNESDAY', 'WEDNESDAY'),
        ('THURSDAY', 'THURSDAY'),
        ('FRIDAY', 'FRIDAY'),
        ('SATURDAY', 'SATURDAY'),
        ('SUNDAY', 'SUNDAY'),
    )
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    barber = models.ForeignKey(
        Barbers,
        on_delete=models.CASCADE,
        db_column='barber_id',
        related_name='schedules'
    )
