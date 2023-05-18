# Portfolio
*Technical Assessment

## Technologies
- Django
- GeoDjango
- Leaflet
- PostGIS

## Run the Application

Database settings:
- ENGINE: The database engine this case, 'django.contrib.gis.db.backends.postgis' requires that the PostGIS spatial database backend should be used.
- Check settings.py for database configurations and update the configs accordingly

GDAL, GEOS & PROJ Configurations
- Make sure you have installed GDAL and PROJ and if you are using windows it's easy to install using OSGeo4W
- Check bottom of settings.py for GEOS_LIBRARY_PATH and GDAL_LIBRARY_PATH and make sure the 2 are compatible

Create a virtual environment and activate it
Navigate to the root of the project and run below commands :

``` pip install -r requirements.txt```
``` python manage.py migrate```
``` python manage.py createsuperuser```
``` python manage.py runserver```

## Improvements Needed to the Application
- Enabling CI Integration
- Validation
- Showing map on edit profile for all users. Currently the map is showing when editing user as superadmin

## Test Cases
- There are test cases for both models and views in portfolio_app/tests.py
- To run the tests, run the following command:
``` python manage.py test```

- I have attached a screenshot showing that all 19 tests passed 

## Managing Content
- Login as super admin http://127.0.0.1:8000/admin 
- Start adding projects, experience and skills
- The portfolio http://127.0.0.1:8000 should be updated

## Authorization
- When you get to the portfolio home page you won't see map and profile links in the navbar (menu) until you sign in.
- You won't be able to view map for the locations of users if you are not a superadmin

## Screenshots

![tests](https://i.imgur.com/abcdefg.png)

