from rest_framework import serializers
from astro_objects.models import AstronomicalObject, DataRelease

class DataReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRelease
        fields = ['id', 'name', 'pretty_name', 'version']

class AstronomicalObjectSerializer(serializers.ModelSerializer):
    data_release = DataReleaseSerializer(read_only=True)

    class Meta:
        model = AstronomicalObject
        fields = ['id', 'right_ascension', 'declination', 'source_name', 'data_release']
         
    #def validate_right_ascension(self, value):
    #    if not (0 <= value <= 360):
    #        raise serializers.ValidationError("Right Ascension must be between 0 and 360 degrees.")
    #    return value