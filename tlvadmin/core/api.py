from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User

# User Viewset
class UserViewSet(viewsets.ModelViewSet):    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    