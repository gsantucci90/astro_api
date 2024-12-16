from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from astro_objects.models import AstronomicalObject
from astro_objects.serializers import AstronomicalObjectSerializer


class AstronomicalObjectListView(generics.ListAPIView):
    """
    List all astronomical objects.

    GET request to this view returns a list of all astronomical objects.
    
    """
    queryset = AstronomicalObject.objects.all().order_by('id') 
    serializer_class = AstronomicalObjectSerializer


class AstronomicalObjectDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific astronomical object.

    GET request to this view returns the details of an individual astronomical object.
    The object is retrieved based on the 'id' provided in the URL.
    """
    queryset = AstronomicalObject.objects.all()
    serializer_class = AstronomicalObjectSerializer
    

       
@api_view(['GET'])
def api_root(request, format=None):
    """
    Retrieve the root of the API.

    This is the entry point for the API. It provides a link to the available endpoints.
    """
    return Response({
        'astro_objects': reverse('astro_objects_list', request=request, format=format)
    })    