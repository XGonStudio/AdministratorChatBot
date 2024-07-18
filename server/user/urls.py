from django.urls import path
from .views import *

urlpatterns = [
    path('api/list', UserListAPI.as_view(), name='api-user-list'),
    path('list', UserListView.as_view(), name='user-list'),
    path('<int:pk>', UserDetailView.as_view(), name='user-detail')
]
