Django Units [WIP]
==================

A Django app to convert units between different systems.

This app is created to simplify the storage and conversion of values of
different messurement systems. Focussing on the conversion between the imperial
and the metrical system the overall goal is, to allow storing either of the
two system's value and having access to the other.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-units

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-units.git#egg=units

TODO: Describe further installation steps (edit / remove the examples below):

Add ``units`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'units',
    )

Add the ``units`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^units/', include('units.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load units_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate units


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-units
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
