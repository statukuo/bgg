from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Booking, Table, Member
from django.contrib.auth.password_validation import validate_password

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
        fields = ['url', 'title', 'description', 'creator', 'max_participants', 'start_date', 'end_date', 'attendants']

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ['url', 'name', 'description', 'active']

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
