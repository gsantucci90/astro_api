from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from astro_objects.models import AstronomicalObject
from astro_objects.serializers import AstronomicalObjectSerializer

class AstronomicalObjectListView(generics.ListAPIView):
    queryset = AstronomicalObject.objects.all()
    serializer_class = AstronomicalObjectSerializer

class AstronomicalObjectDetailView(generics.RetrieveAPIView):
    queryset = AstronomicalObject.objects.all()
    serializer_class = AstronomicalObjectSerializer
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'astro_objects': reverse('astro_objects_list', request=request, format=format)
    })    