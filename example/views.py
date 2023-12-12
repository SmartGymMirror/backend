from django.http import JsonResponse
from django.http import HttpResponse
import requests

def get_weather(request):
    localizacion = request.GET.get('localizacion')

    if not localizacion:
        return JsonResponse({'error': 'Debes especificar una localización'}, status=400)
    
    api_key ='059dca98c3a6e58e739c8a0d2716d00f' # Aquí va tu API KEY de OpenWeatherMap
    weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?q={localizacion}&appid={api_key}&units=metric&lang=es'

    try:
        response=requests.get(weather_api_url)
        return HttpResponse(response, status=200)
    except requests.exceptions.HTTPError as errh:
        return JsonResponse({'error': f'Error HTTP: {errh}'}) 
    except requests.exceptions.RequestException as err:
        return JsonResponse({'error': f'Error de solicitud: {err}'}, status=500)

from django.http import JsonResponse

def datos_ficticios(request):
    datos_ficticios = [
        {
            "timestamp": '2023-12-11T08:18:20.665807Z',
            "weight": '70.00',
            "muscular_mass": '35.00',
            "body_fat": '15.60',
        },
        {
            "timestamp": '2023-12-12T08:18:34.566000Z',
            "weight": '70.50',
            "muscular_mass": '35.50',
            "body_fat": '16.00',
        },
        {
            "timestamp": '2023-12-13T08:18:49.527000Z',
            "weight": '72.50',
            "muscular_mass": '30.50',
            "body_fat": '14.00',
        },
        {
            "timestamp": '2023-12-14T08:18:59.103000Z',
            "weight": '72.50',
            "muscular_mass": '36.00',
            "body_fat": '14.00',
        },
        {
            "timestamp": '2023-12-15T08:19:07.082000Z',
            "weight": '72.50',
            "muscular_mass": '40.00',
            "body_fat": '16.20',
        },
    ]
    return JsonResponse(datos_ficticios, safe=False)

def test_cors(request):
    response = JsonResponse({'message': 'CORS test successful'})
    return response