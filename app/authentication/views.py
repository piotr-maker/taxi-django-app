from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permision_classes = [IsAdminUser]


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permision_classes = [IsAdminUser]
