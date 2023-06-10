"""
URL configuration for django_models project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from person_info import views
# Para la configuracion media url.
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', views.mostrar_personas, name='mostrar_personas'),
    path('home/', views.home, name='home_page'),
    path('hello_world/', views.hello_world, name='hello_world'),
# agrega la configuracion:media_url.Esto permitirá que Django sirva los archivos de medios correctamente en tu aplicación.
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
