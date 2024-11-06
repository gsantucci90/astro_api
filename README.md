A simple REST API with Django Rest Framework (https://www.django-rest-framework.org/) for managing a database of astronomical objects. 
Each object has the following properties:<br />
<br />
**Astronomical Object ID** (primary key) <br />
**Right Ascension** (float) <br />
**Declination** (float) <br />
**Source Name** (string) <br />
**Data Release** (foreign key)<br />
<br />
**Data Release ID** (primary key) <br />
**Name** (string) <br />
**Pretty Name** (string) <br />
**Version** (float) <br />
<br />
This is a read-only set of endpoints (ie list, retrieve only); a user should be able to request a representation of all astronomical objects in the database via /api/astro_objects and a singular entity at /api/astro_objects/<id> 
