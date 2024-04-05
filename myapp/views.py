from .models import CustomUser, Todo
from .permissions import IsTodoOwner, IsOwner
from .serializers import CustomUserSerializer, TodoSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .paginations import TodoPageNumberPagination


# Create your views here.
class TodoAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = TodoPageNumberPagination

    def get_queryset(self):
        data = Todo.objects.filter(user=self.request.user)
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SingleTodoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTodoOwner]


class RegisterUserAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


class UserAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    # filter_backends = [DjangoFilterBackend]    # Can use it Locally but applied globally in settings inside Rest_Framework
    filterset_fields = ("email", "id")


class SingleCustomUserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
