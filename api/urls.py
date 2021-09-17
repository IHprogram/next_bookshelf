from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView

router = routers.DefaultRouter()

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]