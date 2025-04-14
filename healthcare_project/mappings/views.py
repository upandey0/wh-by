from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PatientDoctorsListView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        # Get mappings for the patient
        mappings = PatientDoctorMapping.objects.filter(
            patient_id=patient_id, 
            created_by=self.request.user
        )
        # Extract the doctor IDs
        doctor_ids = mappings.values_list('doctor_id', flat=True)
        # Return the doctors
        return Doctor.objects.filter(id__in=doctor_ids)