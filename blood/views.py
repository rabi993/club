from rest_framework import generics
from .models import Blood
from .serializers import BloodSerializer

class BloodListView(generics.ListAPIView):
    queryset = Blood.objects.select_related('user', 'person').all()
    serializer_class = BloodSerializer

class BloodDetailView(generics.RetrieveAPIView):
    queryset = Blood.objects.select_related('user', 'person').all()
    serializer_class = BloodSerializer

