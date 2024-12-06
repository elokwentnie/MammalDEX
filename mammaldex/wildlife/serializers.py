from rest_framework import serializers
from .models import Mammal, Region, Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = Region
        fields = ['id', 'name', 'country']

class MammalSerializer(serializers.ModelSerializer):
    regions = RegionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Mammal
        fields = [
            'id', 'name', 'latin_name', 'weight', 'height', 'pregnancy_period',
            'lifespan', 'description', 'diet', 'lifestyle', 'regions'
        ]
