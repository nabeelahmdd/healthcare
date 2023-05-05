from django.db import models

# Create your models here.
from django.db import models
from custom.models import User


class MedicalRecord(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    medical_history = models.TextField()
    allergies = models.TextField()
    current_medications = models.TextField()
    blood_type = models.CharField(max_length=5)
    weight = models.FloatField()
    height = models.FloatField()
    soft_delete = models.BooleanField(default=False)
    cr_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="medical_record_cr_by")
    up_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="medical_record_up_by")

    def _str_(self):
        return f"Medical record for {self.patient}"


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('R', 'Rescheduled'),
        ('X', 'Cancelled'),
    )
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    reason = models.TextField()
    soft_delete = models.BooleanField(default=False)
    cr_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="appointment_cr_by")
    up_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="appointment_up_by")

    def _str_(self):
        return f"Appointment for {self.patient} with {self.doctor}"


class Specialty(models.Model):
    specialty = models.CharField(max_length=50)
    soft_delete = models.BooleanField(default=False)
    cr_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="specialty_cr_by")
    up_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="specialty_up_by")

    def _str_(self):
        return self.specialty


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    soft_delete = models.BooleanField(default=False)
    cr_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="doctor_cr_by")
    up_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="doctor_up_by")

    def _str_(self):
        return f"{self.user.first_name} {self.user.last_name}, {self.specialty}"
