from django.urls import path
from .views import PostView


urlpatterns = [
    path("news/", PostView.as_view()),
    path("news/<int:pk>", PostView.as_view()), 
]
