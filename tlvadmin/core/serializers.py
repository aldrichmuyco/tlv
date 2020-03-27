from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User

# Users Serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        datatables_always_serialize = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'], 
            password = make_password(validated_data['password']))
        return user