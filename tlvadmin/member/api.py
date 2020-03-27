from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import ProvinceSerializer
from .models import Province

# Province Viewset API
class ProvinceViewSet(viewsets.ModelViewSet):    
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()
    