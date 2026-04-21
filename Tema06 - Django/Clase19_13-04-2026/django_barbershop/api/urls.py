from django.urls import path
from services.views import (
    ServicesView,
    ManageServicesView,
    BarbersView,
    ManageBarbersView,
    BarberAvailableView,
    SchedulesView,
    ManageSchedulesView,
)

urlpatterns = [
    path('services/', ServicesView.as_view()),
    path('services/<int:pk>/', ManageServicesView.as_view()),
    
    path('barbers/', BarbersView.as_view()),
    path('barbers/<int:pk>/', ManageBarbersView.as_view()),
    path('barbers/available/', BarberAvailableView.as_view()),

    path('schedules/', SchedulesView.as_view()),
    path('schedules/<int:pk>/', ManageSchedulesView.as_view()),
]