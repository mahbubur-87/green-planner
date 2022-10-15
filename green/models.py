from django.db import models

# Create your models here.
class Route(models.Model):
    location_from = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
    route_type = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    travel_time_in_min = models.PositiveIntegerField()
    transit = models.PositiveIntegerField()
    price = models.FloatField()
    currency = models.CharField(max_length=10)
    fuel_type = models.CharField(max_length=20)
    co2_emission_kg = models.FloatField()
    water_consumption_rating = models.PositiveIntegerField()
    waste_management_rating = models.PositiveIntegerField()

class Stay(models.Model):
    name = models.CharField(max_length=200)
    stay_type = models.CharField(max_length=40)
    room_type = models.CharField(max_length=40)
    price_per_night = models.FloatField()
    currency = models.CharField(max_length=10)
    distance_from_airport_km = models.FloatField()
    city = models.CharField(max_length=40)
    co2_emission_kg = models.FloatField()
    water_consumption_rating = models.PositiveIntegerField()
    waste_management_rating = models.PositiveIntegerField()

class Package(models.Model):
    location_from = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
    package_rank = models.PositiveIntegerField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE)