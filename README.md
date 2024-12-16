# Astronomy API

A simple REST API with Django Rest Framework (https://www.django-rest-framework.org/) for managing a database of astronomical objects. 
Each object has the following properties:<br />
<br />
**Astronomical Object** <br />
**ID** (primary key) <br />
**Right Ascension** (float) <br />
**Declination** (float) <br />
**Source Name** (string) <br />
**Data Release** (foreign key)<br />
<br />
**Data Release** <br />
**ID** (primary key) <br />
**Name** (string) <br />
**Pretty Name** (string) <br />
**Version** (float) <br />
<br />
This is a read-only set of endpoints (ie list, retrieve only); a user should be able to request a representation of all astronomical objects in the database via /api/astro_objects and a singular entity at /api/astro_objects/<id> 


## Requirements

- Python 3.9+
- Django 4.2+
- Django REST Framework 3.13+
- SQLite (or another database for production)

## Setup

Follow these steps to set up and run the app locally:

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/astro-api.git
cd astro-api

2. Create and activate a virtual environment
Create a virtual environment to manage dependencies:


# On Windows
python -m venv env
env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate

3. Install the required dependencies
Install the required Python packages using pip:

pip install -r requirements.txt

4. Configure the database
Run migrations to set up the database:

# Set up the database schema
python manage.py makemigrations
python manage.py migrate

6. Load the test dataset
If you want to test the app with a test dataset, you can load it by using the load_astronomical_data command in the following way:

python manage.py load_astronomical_data test_data/astronomical_data.json

6. Run the development server
Start the development server:

python manage.py runserver

Now, you can access the API at:
http://127.0.0.1:8000

The API is available at:

/api/astro_objects/ - List all astronomical objects
/api/astro_objects/<id>/ - Retrieve a specific astronomical object
/ - API root with links to endpoints

7. Running tests
To run the tests for the app:
python manage.py test

API Documentation
The API is documented using Swagger. To view the interactive documentation, navigate to:
http://127.0.0.1:8000/swagger/


License
This project is licensed under the MIT License - see the LICENSE file for details.

Troubleshooting
If you run into any issues, check the following:

Make sure you have Python 3.9 or higher installed.
Ensure that all dependencies are installed using pip install -r requirements.txt.
If running tests fails, ensure that migrations have been run (python manage.py migrate).
If you encounter errors related to URL resolution, double-check that your URL configurations match the expected patterns.
