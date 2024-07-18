from django.urls import path
from .views import *


urlpatterns = [
    path('record', RecordEventView.as_view(), name='record')
]