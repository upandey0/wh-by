from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'doctor', 'assigned_date', 'notes', 
                  'created_at', 'updated_at', 'patient_details', 'doctor_details')
        read_only_fields = ('created_by', 'assigned_date', 'created_at', 'updated_at')

    def validate(self, attrs):
        # Ensure the patient belongs to the current user
        patient = attrs.get('patient')
        request = self.context.get('request')
        
        if patient and patient.created_by != request.user:
            raise serializers.ValidationError(
                {"patient": "You can only assign doctors to your own patients."})
        
        return attrs

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)