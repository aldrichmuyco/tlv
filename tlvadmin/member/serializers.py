from rest_framework import serializers

from .models import Province, City

# Province Serializer
class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = '__all__'