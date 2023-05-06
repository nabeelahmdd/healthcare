from rest_framework.routers import DefaultRouter
from django.urls import path, include
from custom.views.user_views import (
    MyTokenObtainPairView, RegisterView,
)
from custom.views.clinic_views import (
    ClinicView
)
from custom.views.receptionist_views import (
    ReceptionistView
)
router = DefaultRouter()

router.register('register', RegisterView,
                basename='register')
router.register('clinic', ClinicView,
                basename='clinic')
router.register('receptionist', ReceptionistView,
                basename='receptionist')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(),
         name='login'),
]
