from rest_framework import mixins, viewsets
from custom.serializers.clinic_serializer import (
    ClinicSerializer,
)
from custom.models import Clinic
from custom.permissions import IsDoctor
from custom.mixins import CustomDestroyMixin


class ClinicView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    CustomDestroyMixin,
    viewsets.GenericViewSet,
):
    """
    only doctor can perform crud operation on clinic,
    get clinic where soft_delete is False or doctor is associated with it
    """
    permission_classes = (IsDoctor,)
    serializer_class = ClinicSerializer

    def get_queryset(self):
        return Clinic.objects.filter(soft_delete=False,  user=self.request.user)

    def perform_create(self, serializer):
        response = super().perform_create(serializer)
        instance = serializer.instance

        user = self.request.user
        user.clinic = instance
        user.save()
        serializer.save(cr_by=user)

    def perform_update(self, serializer):
        serializer.save(up_by=self.request.user)
