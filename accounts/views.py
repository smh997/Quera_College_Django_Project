from rest_framework import generics
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class LogoutAPIView(APIView):
    pass


class UserRegistration(CreateAPIView):

    def get_serializer_class(self):
        self.serializer_class = UserSerializer
        return self.serializer_class



