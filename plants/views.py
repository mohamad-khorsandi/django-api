from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from plants.serializers import PlantSerializer
from . import serializers
from .models import Plant


class PlantFilterAPI(ListAPIView):
    serializer_class = PlantSerializer
    permission_classes = [AllowAny]
    # It can be safely remove if we only use get_queryset function
    queryset = Plant.objects.filter(is_valid=True)
    lookup_url_kwarg = ['type', 'light_intensity', 'temperature', 'location_type', 'water', 'growth',
                        'attention_need', 'season', 'is_seasonal', 'fragrance', 'pet_compatible',
                        'allergy_compatible', 'edible', ]

    def get_queryset(self):
        filter = {'is_valid': True}
        for field in self.lookup_url_kwarg:
            if self.request.query_params.get(field) and self.request.query_params[field] != '':
                filter[field] = self.request.query_params[field]
        return Plant.objects.filter(**filter)


class PlantDetails(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.PlantSerializer
    queryset = Plant.objects.filter(is_valid=True)
    lookup_field = 'id'
