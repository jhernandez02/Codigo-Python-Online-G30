from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>/', ManagePostView.as_view())
]