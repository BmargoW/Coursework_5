from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer


# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
   # permission_classes = (IsAuthenticated, )

class UserRetrieve(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    #permission_classes = [IsAuthenticated]

class UserUpdate(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    #permission_classes = [IsAuthenticated]

class UserDestroy(generics.DestroyAPIView):
    queryset = User.objects.all()
    #permission_classes = [IsAuthenticated]