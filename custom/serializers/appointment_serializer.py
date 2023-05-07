from rest_framework import serializers
from base.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = [
            'id', 'doctor', 'date', 'time', 'clinic', 'status', 'reason'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view = self.context.get('view')

        if 'view' in self.context and self.context['view'].action in ['create', 'update']:
            # Exclude fields for create view
            self.fields.pop('clinic')
            self.fields.pop('status')
            self.fields.pop('reason')
            if self.context['view'].action == 'update':
                self.fields.pop('doctor')
