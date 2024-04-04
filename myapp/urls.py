from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    TodoAPIView,
    SingleTodoAPIView,
    RegisterUserAPIView,
    SingleCustomUserAPIView,
    UserAPIView,
)

urlpatterns = [
    path("todos/", TodoAPIView.as_view()),
    path("todos/<int:pk>/", SingleTodoAPIView.as_view()),
    path("users/", UserAPIView.as_view()),
    path("users/<int:pk>/", SingleCustomUserAPIView.as_view()),
    path("auth/register/", RegisterUserAPIView.as_view()),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
