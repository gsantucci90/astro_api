import json

# Example data, structured as a list of dictionaries for astronomical objects
data = [
    {
        
        "right_ascension": 150.1,
        "declination": -20.5,
        "source_name": "Object1",
        "data_release": {
           
            "name": "Release 1",
            "pretty_name": "First Release",
            "version": 1.0
        }
    },
    {
       
        "right_ascension": 130.3,
        "declination": -22.1,
        "source_name": "Object2",
        "data_release": {
         
            "name": "Release 2",
            "pretty_name": "Second Release",
            "version": 1.1
        }
    },
    
    {
        
        "right_ascension": 130.3,
        "declination": -22.1,
        "source_name": "Object2",
        "data_release": {
           
            "name": "Release 2",
            "pretty_name": "Second Release",
            "version": 1.1
        }
    },
    
    {
        
        "right_ascension": 130.3,
        "declination": -22.1,
        "source_name": "Object2",
        "data_release": {
           
            "name": "Release 2",
            "pretty_name": "Second Release",
            "version": 1.1
        }
    },
    
    {
        
        "right_ascension": 1330.3,
        "declination": -222.1,
        "source_name": "Object2",
        "data_release": {
           
            "name": "Release 3",
            "pretty_name": "Third Release",
            "version": 1.13
        }
    },
    
    {
        
        "right_ascension": 130.32,
        "declination": -22.31,
        "source_name": "Object2",
        "data_release": {
            
            "name": "Release 3",
            "pretty_name": "Third Release",
            "version": 1.13
        }
    }
]

# Specify the file path where you want to save the JSON data
file_path = 'astronomical_data.json'

# Write the data to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)