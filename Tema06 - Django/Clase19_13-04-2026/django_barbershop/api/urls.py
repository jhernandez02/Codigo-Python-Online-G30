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
from authentication.views import (
    RolesView,
    ManageRolesView,
    UserView,
    ManageUserView,
    UserRoleView,
)
from transactions.views import AppointmentsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('services/', ServicesView.as_view()),
    path('services/<int:pk>/', ManageServicesView.as_view()),
    
    path('barbers/', BarbersView.as_view()),
    path('barbers/<int:pk>/', ManageBarbersView.as_view()),
    path('barbers/available/', BarberAvailableView.as_view()),

    path('schedules/', SchedulesView.as_view()),
    path('schedules/<int:pk>/', ManageSchedulesView.as_view()),

    path('roles/', RolesView.as_view()),
    path('roles/<int:pk>/', ManageRolesView.as_view()),
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', ManageUserView.as_view()),
    path('users/roles/', UserRoleView.as_view()),

    path('auth/login/', TokenObtainPairView.as_view()),

    path('appointments/', AppointmentsView.as_view()),
]