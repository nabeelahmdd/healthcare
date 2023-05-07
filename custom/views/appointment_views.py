from rest_framework import mixins, viewsets
from custom.serializers import (
    AppointmentSerializer,
)
from base.models import Appointment
from rest_framework.permissions import IsAuthenticated
from custom.mixins import CustomDestroyMixin


class AppointmentView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    CustomDestroyMixin,
    viewsets.GenericViewSet,
):
    """
    only doctor can perform crud operation on appointment,
    get appointment where soft_delete is False or doctor is associated with it
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(soft_delete=False,  patient=self.request.user)

    def perform_create(self, serializer):
        response = super().perform_create(serializer)
        instance = serializer.instance

        user = self.request.user
        serializer.save(
            cr_by=user, clinic=instance.doctor.user.clinic, status='P',
            patient=user
        )

    def perform_update(self, serializer):
        serializer.save(up_by=self.request.user)
