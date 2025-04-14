from django.urls import path
from .views import PatientDoctorMappingViewSet, PatientDoctorsListView

urlpatterns = [
    path('', PatientDoctorMappingViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', PatientDoctorMappingViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path('<int:patient_id>/', PatientDoctorsListView.as_view(), name='patient-doctors'),
]