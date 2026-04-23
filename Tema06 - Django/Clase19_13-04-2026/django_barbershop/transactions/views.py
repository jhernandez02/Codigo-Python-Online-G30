from rest_framework import generics
from .models import Appointments
from .serializers import AppointmentSerializer

class AppointmentsView(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer