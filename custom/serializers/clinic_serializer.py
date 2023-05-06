from rest_framework import serializers
from custom.models import Clinic


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        exclude = [
            'soft_delete', 'cr_by', 'up_by'
        ]
