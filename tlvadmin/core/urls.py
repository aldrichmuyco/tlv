from django.urls import path
from rest_framework import routers
from .api import UserViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/rest/users', UserViewSet)

urlpatterns = [
    path('users/', views.users, name='users'),
]

urlpatterns += router.urls