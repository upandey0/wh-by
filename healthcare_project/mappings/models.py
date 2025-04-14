from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMapping(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mappings')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')
    assigned_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f"{self.patient} assigned to {self.doctor}"