from django.urls import path
from rest_framework import routers
from .api import ProvinceViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/rest/address/province', ProvinceViewSet)

urlpatterns = [
    path('address/', views.address, name='address'),
]

urlpatterns += router.urls