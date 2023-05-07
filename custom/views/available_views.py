from rest_framework import mixins, viewsets
from custom.serializers import (
    AvailabilitySerializer,
)
from base.models import Availability
from custom.permissions import IsDoctor
from custom.mixins import CustomDestroyMixin


class AvailabilityView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    CustomDestroyMixin,
    viewsets.GenericViewSet,
):
    """
    only doctor can perform crud operation on Availability,
    get Availability where soft_delete is False or doctor is associated with it
    """
    permission_classes = (IsDoctor,)
    serializer_class = AvailabilitySerializer

    def get_queryset(self):
        return Availability.objects.filter(soft_delete=False,  doctor__user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(cr_by=user, doctor=user.doctor_set.all().first())

    def perform_update(self, serializer):
        serializer.save(up_by=self.request.user)
