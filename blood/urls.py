from django.urls import path
from .views import BloodListView, BloodDetailView

urlpatterns = [
    path('blood/', BloodListView.as_view(), name='blood-list'),  # List all blood records
    path('blood/<int:pk>/', BloodDetailView.as_view(), name='blood-detail'),  # Retrieve a specific blood record by ID
]
