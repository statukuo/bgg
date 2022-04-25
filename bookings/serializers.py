from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Booking, Table, Member

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['alias']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'member']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['url', 'title', 'description', 'creator', 'max_participants', 'start_date', 'end_date', 'attendants', 'table']

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ['url', 'name', 'description', 'active']
