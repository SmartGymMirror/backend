from django.urls import path
from .views import get_weather, test_cors

urlpatterns = [
    path('weather/', get_weather, name='get_weather'),
    path('test-cors/', test_cors, name='test_cors'),
]
