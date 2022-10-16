from django.urls import path
from .views import RouteViews, StayViews, PackageViews

urlpatterns = [
    path('routes/', RouteViews.as_view()),
    path('routes/<int:id>', RouteViews.as_view()),
    path('stays/', StayViews.as_view()),
    path('stays/<int:id>', StayViews.as_view()),
    path('packages/', PackageViews.as_view()),
    path('packages/<int:id>', PackageViews.as_view()),
    path('packages/<str:location_from>/<str:location_to>', PackageViews.as_view()),
]