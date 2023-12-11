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

def test_cors(request):
    response = JsonResponse({'message': 'CORS test successful'})
    return response