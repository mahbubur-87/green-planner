from django.contrib import admin
from .models import Route, Stay, Package

# Register your models here.
admin.site.register(Route)
admin.site.register(Stay)
admin.site.register(Package)
