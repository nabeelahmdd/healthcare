from rest_framework.routers import DefaultRouter
from django.urls import path, include
from custom.views.user_views import (
    MyTokenObtainPairView, RegisterView,
)

router = DefaultRouter()

router.register('register', RegisterView,
                basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(),
         name='login'),
]
