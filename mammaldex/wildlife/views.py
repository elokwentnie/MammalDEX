from rest_framework import generics
from .models import Mammal, Region
from .serializers import MammalSerializer

class MammalListView(generics.ListAPIView):
    queryset = Mammal.objects.all()
    serializer_class = MammalSerializer

class MammalByRegionView(generics.ListAPIView):
    serializer_class = MammalSerializer

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return Mammal.objects.filter(regions__id=region_id)
