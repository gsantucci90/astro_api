import json
from django.core.management.base import BaseCommand
from astro_objects.models import AstronomicalObject, DataRelease

class Command(BaseCommand):
    help = 'Load astronomical data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the JSON file.")

    def handle(self, *args, **kwargs):
        # Open your JSON dataset 
        file_path = kwargs['file_path']
        try:
            with open(file_path, newline='') as jsonfile:
                data = json.load(jsonfile)

                # Iterate over the data and load objects
                for obj_data in data:
                    # Get or create the DataRelease object based on the "name" to avoid duplicates
                    data_release, created = DataRelease.objects.get_or_create(
                        name=obj_data['data_release']['name'],
                        pretty_name=obj_data['data_release']['pretty_name'],
                        version=obj_data['data_release']['version']
                    )
    
                    # Create the AstronomicalObject instance and link it to the DataRelease
                    AstronomicalObject.objects.create(
                        right_ascension=obj_data['right_ascension'],
                        declination=obj_data['declination'],
                        source_name=obj_data['source_name'],
                        data_release=data_release
                    )
                       
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data: {e}'))
