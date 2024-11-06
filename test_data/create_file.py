import json

# Example data, structured as a list of dictionaries for astronomical objects
data = [
    {
        "id": 1,
        "right_ascension": 150.1,
        "declination": -20.5,
        "source_name": "Object1",
        "data_release": {
            "id": 1,
            "name": "Release 1",
            "pretty_name": "First Release",
            "version": 1.0
        }
    },
    {
        "id": 2,
        "right_ascension": 130.3,
        "declination": -22.1,
        "source_name": "Object2",
        "data_release": {
            "id": 2,
            "name": "Release 2",
            "pretty_name": "Second Release",
            "version": 1.1
        }
    },
    
    {
        "id": 3,
        "right_ascension": 130.3,
        "declination": -22.1,
        "source_name": "Object2",
        "data_release": {
            "id": 3,
            "name": "Release 2",
            "pretty_name": "Second Release",
            "version": 1.1
        }
    },
    
    {
        "id": 4,
        "right_ascension": 130.3,
        "declination": -22.1,
        "source_name": "Object2",
        "data_release": {
            "id": 4,
            "name": "Release 2",
            "pretty_name": "Second Release",
            "version": 1.1
        }
    },
    
    {
        "id": 5,
        "right_ascension": 1330.3,
        "declination": -222.1,
        "source_name": "Object2",
        "data_release": {
            "id": 5,
            "name": "Release 2",
            "pretty_name": "Second Release",
            "version": 1.13
        }
    },
    
    {
        "id": 6,
        "right_ascension": 130.32,
        "declination": -22.31,
        "source_name": "Object2",
        "data_release": {
            "id": 6,
            "name": "Release 2",
            "pretty_name": "Second Release",
            "version": 1.13
        }
    }
]

# Specify the file path where you want to save the JSON data
file_path = 'astronomical_data.json'

# Write the data to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)