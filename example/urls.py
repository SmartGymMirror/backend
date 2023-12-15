from django.urls import path
from .views import get_weather, test_cors, datos_ficticios, squat_counter

urlpatterns = [
    path('weather/', get_weather, name='get_weather'),
    path('test-cors/', test_cors, name='test_cors'),
    path('datos-ficticios/', datos_ficticios, name='datos_ficticios'),
    path('squat-counter/', squat_counter, name='squat_counter')

]
