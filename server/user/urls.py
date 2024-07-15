from django.urls import path
from .views import *

urlpatterns = [
    path('api/list', UserListAPI.as_view(), name='api-user-list'),
]
