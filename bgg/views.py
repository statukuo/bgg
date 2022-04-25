from .serializers import ChangePasswordSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
