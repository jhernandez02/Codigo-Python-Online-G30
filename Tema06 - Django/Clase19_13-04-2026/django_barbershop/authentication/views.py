from rest_framework import generics
from .models import (
    Roles,
    UserRoles,
)
from .serializers import (
    RoleSerializer,
    UserSerializer,
    UserRoleSerializer,
)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class RolesView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer

class ManageRolesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserRoleView(generics.ListCreateAPIView):
    queryset = UserRoles.objects.all()
    serializer_class = UserRoleSerializer