from rest_framework import serializers
from astro_objects.models import AstronomicalObject, DataRelease

class DataReleaseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the DataRelease model with hyperlinks.
    
    Fields:
    - id: Primary key for the data release.
    - name: Name of the data release.
    - pretty_name: Display name for the data release.
    - version: Version number of the data release.
    """
    class Meta:
        model = DataRelease
        fields = ['id', 'name', 'pretty_name', 'version']
        extra_kwargs = {
            'name': {'help_text': 'The name of the data release.'},
            'pretty_name': {'help_text': 'A more user-friendly display name for the data release.'},
            'version': {'help_text': 'The version of the data release.'},
           
        }
    
    def to_representation(self, instance):
        """
        Renames the fields with pretty names
        """
        representation = super().to_representation(instance)
        # Rename fields
        renamed_representation = {
           
            "ID": representation["id"],
            "Name": representation["name"],
            "Pretty Name": representation["pretty_name"],
            "Version": representation["version"]
        }
        return renamed_representation
        
        
        
class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the AstronomicalObject model with hyperlinks.

    Fields:
    - url: Hyperlink to the object
    - id: Primary key for the astronomical object.
    - right_ascension: Right ascension coordinate in degrees.
    - declination: Declination coordinate in degrees.
    - source_name: The source name of the object.
    - data_release: The related data release information.
    - user: The user who created the object (hidden from input).
    """
    data_release = DataReleaseSerializer(read_only=True)

    class Meta:
        model = AstronomicalObject
        fields = ['url','id', 'right_ascension', 'declination', 'source_name', 'data_release']
        extra_kwargs = {
            'source_name': {'help_text': 'The name of the astronomical object.'},
            'right_ascension': {'help_text': 'The right ascension of the astronomical object in degrees.'},
            'declination': {'help_text': 'The declination of the astronomical object in degrees.'},
            'url': {'view_name': 'astronomicalobject-detail'},
        }
        
    def to_representation(self, instance):
        """
        Renames the fields with pretty names
        """
        representation = super().to_representation(instance)
        # Rename fields
        renamed_representation = {
            "Url": representation["url"],
            "ID": representation["id"],
            "Right Ascension": representation["right_ascension"],
            "Declination": representation["declination"],
            "Source Name": representation["source_name"],
            "Data Release": representation["data_release"]
        }
        return renamed_representation