from rest_framework.routers import DefaultRouter
from django.urls import path, include
from custom.views import (
    MyTokenObtainPairView, RegisterView, ClinicView, ReceptionistView,
    AppointmentView, AvailabilityView,
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
router.register('doctor-availabilty', AvailabilityView,
                basename='doctor-availabilty')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(),
         name='login'),
]
