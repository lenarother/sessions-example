How to use sessions
===================


This is a project that demonstrates the basics of Django session framework.

To learn more about sessions in Django please refer to the documentation:
https://docs.djangoproject.com/en/3.1/topics/http/sessions/


Try it out
----------

.. code-block:: bash

    $ # Clone repository
    $ git clone https://github.com/lenarother/sessions-example.git

    $ # Create your virtualenv and install requirements

    $ # Apply initial migrations
    $ cd sessions-example/src
    $ python manage.py migrate

    $ # run tests
    $ cd sessions-example/src
    $ pytest

    $ # run server
    $ cd sessions-example/src
    $ python manage.py runserver
    $ # visit localhost:8000 in your browser
