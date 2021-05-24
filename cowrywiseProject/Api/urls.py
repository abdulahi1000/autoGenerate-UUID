from django.urls import path
from .views import *

urlpatterns = [
    path('', all_data, name='all_data'),
]
