from rest_framework import generics
from .models import Blood
from .serializers import BloodSerializer

class BloodListView(generics.ListAPIView):
    queryset = Blood.objects.all()
    serializer_class = BloodSerializer

class BloodDetailView(generics.RetrieveAPIView):
    queryset = Blood.objects.all()
    serializer_class = BloodSerializer
