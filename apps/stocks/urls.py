from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

defaultRouter = DefaultRouter()
defaultRouter.register('vested_equity_valuation', views.VestedEquityValueViewset, basename='vested-equity-viewsets')
urlpatterns = [
    path('', include(defaultRouter.urls))
]
