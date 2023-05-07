from rest_framework import serializers
from base.models import Availability


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = [
            'id', 'day_of_week', 'zone', 'start_time', 'end_time', 'doctor'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view = self.context.get('view')

        if 'view' in self.context and self.context['view'].action in ['create', 'update']:
            # Exclude fields for create view
            self.fields.pop('doctor')
