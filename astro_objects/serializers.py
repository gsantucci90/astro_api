from rest_framework import serializers
from astro_objects.models import AstronomicalObject, DataRelease

class DataReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRelease
        fields = ['id', 'name', 'pretty_name', 'version']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Rename fields
        renamed_representation = {
            "ID": representation["id"],
            "Name": representation["name"],
            "Pretty Name": representation["pretty_name"],
            "Version": representation["version"]
        }
        return renamed_representation
        
class AstronomicalObjectSerializer(serializers.ModelSerializer):
    data_release = DataReleaseSerializer(read_only=True)

    class Meta:
        model = AstronomicalObject
        fields = ['id', 'right_ascension', 'declination', 'source_name', 'data_release']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Rename fields
        renamed_representation = {
            "ID": representation["id"],
            "Right Ascension": representation["right_ascension"],
            "Declination": representation["declination"],
            "Source Name": representation["source_name"],
            "Data Release": representation["data_release"]
        }
        return renamed_representation