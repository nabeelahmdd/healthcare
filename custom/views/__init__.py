from .user_views import MyTokenObtainPairView, RegisterView
from .clinic_views import ClinicView
from .receptionist_views import ReceptionistView
from .appointment_views import AppointmentView
from .available_views import AvailabilityView

__all__ = ["MyTokenObtainPairView", "RegisterView", "ClinicView",
           "ReceptionistView", "AppointmentView", "AvailabilityView"]
