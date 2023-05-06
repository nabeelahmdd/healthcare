from rest_framework import mixins, viewsets
from custom.serializers.user_serializer import (
    UserSerializer
)
from custom.models import User
from custom.permissions import IsDoctor
from custom.mixins import CustomDestroyMixin


class ReceptionistView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    CustomDestroyMixin,
    viewsets.GenericViewSet,
):
    """
    only doctor can perform crud operation on receptionist,
    get receptionist list where soft_delete is False or doctor clinic 
    and receptionist clinic is same
    """
    permission_classes = (IsDoctor,)
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = User.objects.filter(
            soft_delete=False,  clinic=self.request.user.clinic, category='r'
        )
        return qs

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            cr_by=user, clinic=user.clinic, category='r'
        )

    def perform_update(self, serializer):
        serializer.save(up_by=self.request.user)
