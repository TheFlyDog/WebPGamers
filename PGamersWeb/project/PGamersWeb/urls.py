from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('accounts/', include('django.contrib.auth.urls')), #Urls de autenticacion de la cuenta de usuario
    path('oauth/', include('social_django.urls', namespace='social')), #Urls de red social django
    path('api/',include('Api.urls')),
    path('api_generate_token/', views.obtain_auth_token),
    path('', include('PGamersApp.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)