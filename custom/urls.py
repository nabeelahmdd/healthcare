from rest_framework.routers import DefaultRouter
from django.urls import path, include
from custom.views import (
    MyTokenObtainPairView, RegisterView, ClinicView, ReceptionistView, AppointmentView,
)

router = DefaultRouter()

router.register('register', RegisterView,
                basename='register')
router.register('clinic', ClinicView,
                basename='clinic')
router.register('receptionist', ReceptionistView,
                basename='receptionist')
router.register('appointment', AppointmentView,
                basename='appointment')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(),
         name='login'),
]
