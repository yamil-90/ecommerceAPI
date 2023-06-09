from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static, serve
import os



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView),
    path('api/', include('core.urls', namespace='core')),
    path('api-auth/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve the favicon - Keep for later
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'media/static/'),
        }
    )
]