from .serializers import ChangePasswordSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

class CheckAuth(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message': 'Correct Auth'})
