from django.shortcuts import render
from rest_framework import generics
from .models import (
    Services,
    Barbers,
    Schedules,
)
from .serializers import (
    ServiceSerializer,
    BarberSerializer,
    ScheduleSerializer,
)
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from datetime import time

class ServicesView(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class ManageServicesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class BarbersView(generics.ListCreateAPIView):
    queryset = Barbers.objects.all()
    serializer_class = BarberSerializer

class ManageBarbersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Barbers.objects.all()
    serializer_class = BarberSerializer

class SchedulesView(generics.ListCreateAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

class ManageSchedulesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

@extend_schema(
    parameters=[
        OpenApiParameter(
            name='day_of_week',
            description='Día de la semana (ej: MONDAY)',
            required=True,
            type=OpenApiTypes.STR,
        ),
        OpenApiParameter(
            name='hour',
            description='Hora (ej: 10:00)',
            required=True,
            type=OpenApiTypes.STR,
        )
    ]
)
class BarberAvailableView(generics.ListAPIView):
    serializer_class = BarberSerializer

    def get_queryset(self):
        day_of_week = self.request.query_params.get('day_of_week')
        hour = self.request.query_params.get('hour')
        hour_time = time.fromisoformat(hour)

        return Barbers.objects.filter(
            schedules__day_of_week=day_of_week,
            schedules__start_time__lte=hour_time,
            schedules__end_time__gte=hour_time,
        ).distinct()