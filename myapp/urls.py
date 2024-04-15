from django.urls import path, include

from .views import (
    TodoAPIView,
    SingleTodoAPIView,
    SingleCustomUserAPIView,
    UserAPIView,
)

urlpatterns = [
    path("todos/", TodoAPIView.as_view()),
    path("todos/<int:pk>/", SingleTodoAPIView.as_view()),
    path("users/", UserAPIView.as_view()),
    path("users/<int:pk>/", SingleCustomUserAPIView.as_view()),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
