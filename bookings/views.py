from .models import Booking, Member, Table
from .serializers import BookingSerializer, TableSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TableViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class BookingViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    @action(detail=True, methods=['post'])
    def assist(self, request, pk=None):
        booking = self.get_object()
        print(booking)
        print(request.user.id)
        booking.attendants.add(request.user)
        booking.save()
        return Response({})
    @action(detail=True, methods=['post'])
    def forget(self, request, pk=None):
        booking = self.get_object()
        print(booking)
        print(request.user.id)
        booking.attendants.remove(request.user)
        booking.save()
        return Response({})
