from rest_framework import serializers
from .models import Users


class Users_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['userName', 'stdNum', 'userEmail', 'created']
