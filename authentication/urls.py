from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('web', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth', auth_views.obtain_auth_token)
]