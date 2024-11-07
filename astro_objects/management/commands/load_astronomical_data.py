import json
from django.core.management.base import BaseCommand
from astro_objects.models import AstronomicalObject, DataRelease

class Command(BaseCommand):
    help = 'Load astronomical data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the JSON file.")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, newline='') as jsonfile:
                reader = json.load(jsonfile)
                for row in reader:
                    
                    # Example of loading related data
                    data_release, created = DataRelease.objects.get_or_create(
                        id=row['data_release']['id'],
                        name=row['data_release']['name'],
                        pretty_name=row['data_release']['pretty_name'],
                        version=float(row['data_release']['version'])
                    )

                    AstronomicalObject.objects.get_or_create(
                        id=row['id'],
                        right_ascension=float(row['right_ascension']),
                        declination=float(row['declination']),
                        source_name=row['source_name'],
                        data_release=data_release
                    )
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data: {e}'))
