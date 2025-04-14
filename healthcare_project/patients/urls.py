from django.urls import path
from .views import PatientViewSet

urlpatterns = [
    path('', PatientViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', PatientViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
