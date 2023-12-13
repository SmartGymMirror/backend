from django.http import JsonResponse
from django.http import HttpResponse
import mediapipe as mp
import cv2
import numpy as np
from math import acos, degrees
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

def squat_counter(request):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(0)

    up = False
    down = False
    contador = 0

    with mp_pose.Pose(static_image_mode = False, min_detection_confidence = 0.5) as pose:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            height, width, _ = frame.shape
            frame = cv2.flip(frame,1)
            frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            results = pose.process(frame_rgb)

            if results.pose_landmarks is not None:
                x1 = int(results.pose_landmarks.landmark[24].x * width)
                y1 = int(results.pose_landmarks.landmark[24].y * height)

                x2 = int(results.pose_landmarks.landmark[26].x * width)
                y2 = int(results.pose_landmarks.landmark[26].y * height)

                x3 = int(results.pose_landmarks.landmark[28].x * width)
                y3 = int(results.pose_landmarks.landmark[28].y * height)


                p1 = np.array([x1,y1])
                p2 = np.array([x2,y2])
                p3 = np.array([x3,y3])

                l1 = np.linalg.norm(p2-p3)
                l2 = np.linalg.norm(p1-p3)
                l3 = np.linalg.norm(p1-p2)

                #calcular el angulo
                angle = degrees(acos((l1**2 + l3**2 - l2**2)/(2 * l1 * l3)))

                #contar sentadillas
                if angle >= 160:
                    up = True
                if up == True and down == False and angle <= 70:
                    down = True
                if up == True and down == True and angle >= 160:
                    contador += 1
                    up = False
                    down = False

                print("count",contador)         


                #visualizacion
                cv2.circle(frame,(x1,y1),6,(0,255,255),4)
                cv2.circle(frame,(x2,y2),6,(0,255,255),4)
                cv2.circle(frame,(x3,y3),6,(0,255,255),4)
                aux_image= np.zeros(frame.shape, np.uint8)
                cv2.putText(aux_image,str(int(angle)),(x2 + 30 , y2),1,1.5,(128,0,250),2)
                
                cv2.line(aux_image, (x1,y1),(x2,y2),(255,255,0),20)
                cv2.line(aux_image, (x2,y2),(x3,y3),(255,255,0),20)
                cv2.line(aux_image, (x1,y1),(x3,y3),(255,255,0),5)

                contorno = np.array([[x1,y1],[x2,y2],[x3,y3]])
                output = cv2.addWeighted(frame,1,aux_image,0.8,0)
                cv2.imshow("aux_image",aux_image)    
                cv2.fillPoly(aux_image,pts = [contorno], color=(128,0,250))
                #contador
                cv2.rectangle(frame,(0,0),(60,60),(255,255,0),-1)
                cv2.putText(frame,str(contador),(10,50),1,3.5,(128,0,250),2)
                
            cv2.imshow("Frame",frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()