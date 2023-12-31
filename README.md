
<h1 align="center">Backend</h1>

<h2>Repositorio:</h2>

Aunque este sea el repositorio destinado al backend vamos a subir aquí los enlaces a los demás repositorios para no enviar tantos archivos:

-Link del [backend](https://github.com/albabernal03/ejercicios_parejas_POO)

-Link de [prototipos](https://github.com/SmartGymMirror/prototipos)

-Link de [frontend](https://github.com/SmartGymMirror/frontend) (METERSE AQUÍ PARA PODER VISUALIZAR EL PROYECTO)

-Link de [la primera prueba usuario](https://github.com/lauralardies)

-Link de [la segunda prueba de usuario](https://github.com/SmartGymMirror/usuario)

-Link donde [se probó el backend incialmente](https://github.com/SmartGymMirror/smart_gym_mirror_api)

-Link [prueba chat](https://github.com/SmartGymMirror/chat)

-Link donde se probo [API weather](https://github.com/SmartGymMirror/weather_api)


***


***
## Integrantes

1. [Alba](https://github.com/albabernal03) 
2. [Carlota](https://github.com/crltsnch)
3. [Laura](https://github.com/lauralardies)
4. [Miguel](https://github.com/MiguelGG03)
5. [Ana](https://github.com/AnaLopezP)
6. [Zazo](https://github.com/jzazooro)
7. [Nacho](https://github.com/Nachopedrero)
8. [Andrea](https://github.com/andmansim)
9. [Sergio](https://github.com/dacalite)











[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%204%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)

# Django + Vercel

This example shows how to use Django 4 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://django-template.vercel.app/

## How it Works

Our Django application, `example` is configured as an installed application in `vercel_app/settings.py`:

```python
# vercel_app/settings.py
INSTALLED_APPS = [
    # ...
    'example',
]
```

We allow "\*.vercel.app" subdomains in `ALLOWED_HOSTS`, in addition to 127.0.0.1:

```python
# vercel_app/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
```

The `wsgi` module must use a public variable named `app` to expose the WSGI application:

```python
# vercel_app/wsgi.py
app = get_wsgi_application()
```

The corresponding `WSGI_APPLICATION` setting is configured to use the `app` variable from the `vercel_app.wsgi` module:

```python
# vercel_app/settings.py
WSGI_APPLICATION = 'vercel_app.wsgi.app'
```

There is a single view which renders the current time in `example/views.py`:

```python
# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
```

This view is exposed a URL through `example/urls.py`:

```python
# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    path('', index),
]
```

Finally, it's made accessible to the Django server inside `vercel_app/urls.py`:

```python
# vercel_app/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('example.urls')),
]
```

This example uses the Web Server Gateway Interface (WSGI) with Django to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
python manage.py runserver
```

Your Django application is now available at `http://localhost:8000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%204%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)
