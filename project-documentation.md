# Project Documentation

### Setting up local environment for the project
1. Created project folder *django-library*
2. `cd django-library`
3. Set local environment

    `python3 -m venv .venv`

4. activate the local environment

    `source .venv/bin/activate`

5. install django to the local environment

    `python -m pip install Django`


### Creating new Django project

Created new project *locallibrary* with

`django-admin startproject locallibrary .`

The `.`ensures that the project resides in the same folder as the local environment.

Created the catalog application that lives inside the locallibrary project.

`python3 manage.py startapp catalog`

Registered the catalog app with the project. In `/locallibrary/settings.py` the following line was added to INSTALLED_APPS array:

`'catalog.apps.CatalogConfig',`

The new line specifies the application configuration object (CatalogConfig) that was generated in /locallibrary/catalog/apps.py when you created the application.

Also in `/locallibrary/settings.py`, changed TIME_ZONE to `'Europe/Helsinki'`.

To `locallibrary/urls.py` I added: 

```
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
```

And the root URL was redirected to `'/catalog'`, as this is the only app used in this project.

```
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]
```

Created the `/catalog/urls.py` file with this content:

```
from django.urls import path
from . import views

urlpatterns = [

]

```

To test if everything works properly, first the database migration was run:

````
python3 manage.py makemigrations
python3 manage.py migrate
````

The development web server was run by calling the runserver command (in the same directory as manage.py):

`python3 manage.py runserver`

### Setting up pylint-django properly

Created .pylintrc file by running command:

`python -m pylint --generate-rcfile > .pylintrc`

Added `pylint_django`to `load-plugins=` under `[MAIN]`

Added Django settings section at the bottom of `.pylintrc` file:

```
[DJANGO]
django-settings-module=locallibrary.settings
```

### Models defenition

Models for the catolog app were defined in `/catalog/models.py`. After the models were added, the database migration was re-run to add the models to the database:

```
python manage.py makemigrations
python manage.py migrate
```

### Django admin site
Registered the catalog app models to the admin site by adding them to the admin configuration (/catalog/admin.py).

Created a superuser by running `python manage.py createsuperuser`. Running the server (`python manage.py runserver`) and going to `http://127.0.0.1:8000/admin/` then allows for login as superuser.