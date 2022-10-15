from rest_framework import serializers
from .models import Route, Stay, Package

class RouteSerializer(serializers.ModelSerializer):
    location_from = serializers.CharField(max_length=200)
    location_to = serializers.CharField(max_length=200)
    route_type = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=200)
    travel_time_in_min = serializers.IntegerField(required=False, default=1)
    transit = serializers.IntegerField(required=False, default=0)
    price = serializers.FloatField()
    currency = serializers.CharField(max_length=10)
    fuel_type = serializers.CharField(max_length=20)
    co2_emission_kg = serializers.FloatField()
    water_consumption_rating = serializers.IntegerField(required=False, default=4)
    waste_management_rating = serializers.IntegerField(required=False, default=4)

    class Meta:
        model = Route
        fields = ('__all__')

class StaySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    stay_type = serializers.CharField(max_length=40)
    room_type = serializers.CharField(max_length=40)
    price_per_night = serializers.FloatField()
    currency = serializers.CharField(max_length=10)
    distance_from_airport_km = serializers.FloatField()
    city = serializers.CharField(max_length=40)
    co2_emission_kg = serializers.FloatField()
    water_consumption_rating = serializers.IntegerField(required=False, default=4)
    waste_management_rating = serializers.IntegerField(required=False, default=4)

    class Meta:
        model = Stay
        fields = ('__all__')

class PackageSerializer(serializers.ModelSerializer):
    location_from = serializers.CharField(max_length=200)
    location_to = serializers.CharField(max_length=200)
    package_rank = serializers.IntegerField(required=False, default=1)
    #route = serializers.ForeignKey(Route, on_delete=models.CASCADE)
    #stay = serializers.ForeignKey(Stay, on_delete=models.CASCADE)

    class Meta:
        model = Package
        fields = ('__all__')