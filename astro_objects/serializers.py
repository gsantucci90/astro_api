from rest_framework import serializers
from astro_objects.models import AstronomicalObject, DataRelease

class DataReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRelease
        fields = ['id', 'name', 'pretty_name', 'version']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Rename the field in the output
        representation['ID'] = representation.pop('id')
        representation['Name'] = representation.pop('name')
        representation['Pretty Name'] = representation.pop('pretty_name')
        representation['Version'] = representation.pop('version')
        return representation
        
class AstronomicalObjectSerializer(serializers.ModelSerializer):
    data_release = DataReleaseSerializer(read_only=True)

    class Meta:
        model = AstronomicalObject
        fields = ['id', 'right_ascension', 'declination', 'source_name', 'data_release']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Rename the field in the output
        representation['ID'] = representation.pop('id')
        representation['Right Ascension'] = representation.pop('right_ascension')
        representation['Declination'] = representation.pop('declination')
        representation['Source Name'] = representation.pop('source_name')
        representation['Data Release'] = representation.pop('data_release')
        return representation