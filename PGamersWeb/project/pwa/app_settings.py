""" Settings required by django-app. """
from django.conf import settings
from django.shortcuts import resolve_url
from django.urls import get_script_prefix
from django.utils.functional import lazy
import os

# Lazy-evaluate URLs so including pwa.urls in root urlconf works
resolve_url = lazy(resolve_url, str)

PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH',
                                  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates',
                                               'sw.js'))

# Get script prefix for apps not mounted under /
_PWA_SCRIPT_PREFIX = get_script_prefix()

# App parameters to include in manifest.json and appropriate meta tags
PWA_APP_NAME = getattr(settings, 'PWA_APP_NAME', 'MyApp')
PWA_APP_DESCRIPTION = getattr(settings, 'PWA_APP_DESCRIPTION', 'My Progressive Web App')
PWA_APP_ROOT_URL = resolve_url(getattr(settings, 'PWA_APP_ROOT_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_THEME_COLOR = getattr(settings, 'PWA_APP_THEME_COLOR', '#000')
PWA_APP_BACKGROUND_COLOR = getattr(settings, 'PWA_APP_BACKGROUND_COLOR', '#fff')
PWA_APP_DISPLAY = getattr(settings, 'PWA_APP_DISPLAY', 'standalone')
PWA_APP_SCOPE = resolve_url(getattr(settings, 'PWA_APP_SCOPE', _PWA_SCRIPT_PREFIX))
PWA_APP_DEBUG_MODE = getattr(settings, 'PWA_APP_DEBUG_MODE', True)
PWA_APP_ORIENTATION = getattr(settings, 'PWA_APP_ORIENTATION', 'any')
PWA_APP_START_URL = resolve_url(getattr(settings, 'PWA_APP_START_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_FETCH_URL = resolve_url(getattr(settings, 'PWA_APP_FETCH_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_STATUS_BAR_COLOR = getattr(settings, 'PWA_APP_STATUS_BAR_COLOR', 'default')
PWA_APP_ICONS = getattr(settings, 'PWA_APP_ICONS', [
    { 
        "src": "/static/img/Logo.png",
        "sizes": "40x40" 
    }
])
PWA_APP_SPLASH_SCREEN = getattr(settings, 'PWA_APP_SPLASH_SCREEN', [
    {
        'src': '/static/img/PortadoContacto.png',
        'size': '500x500'
    },
    {
        'src': '/static/img/Contacto.jpg',
        'size': '500x500'
    },
    {
        'src': '/static/img/imagen_slider_1.png',
        'size': '700x700'
    },
    {
        'src': '/static/img/imagen_slider_2.png',
        'size': '700x700'
    },
    {
        'src': '/static/img/imagen_slider_3.png',
        'size': '700x700'
    },
])
PWA_APP_DIR = getattr(settings, 'PWA_APP_DIR', 'auto')
PWA_APP_LANG = getattr(settings, 'PWA_APP_LANG', 'es-es')
