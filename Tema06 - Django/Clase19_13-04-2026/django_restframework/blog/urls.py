from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>/', ManagePostView.as_view()),
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>/', ManageCommentView.as_view())
]