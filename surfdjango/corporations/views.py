from rest_framework import generics
from .models import Corporation
from .serializers import CorporationSerializer

class CorporationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Corporation.objects.all()
    serializer_class = CorporationSerializer
    
class CorporationUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Corporation.objects.all()
    serializer_class = CorporationSerializer

