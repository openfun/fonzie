Getting Started
===============

Fonzie is supposed to be installed as a Django application running in an Open
edX platform instance. Fonzie has been designed to be integrated with the
current Open edX release (Ginkgo at the time of writing). We plan to support the
next Open edX release (Hawthorn) in a near future.

Install dependencies
--------------------

Install fonzie and its dependencies in your Open edX installation with ``pip``:

.. code-block:: bash

    $ (sudo) pip install fonzie


Configure Fonzie
----------------

Once installed, Fonzie needs to be configured as a standard Django application,
*i.e.* adding ``fonzie`` to your ``INSTALLED_APPS`` and Fonzie's URLs to your
project's URLs.

Open edX settings
^^^^^^^^^^^^^^^^^

Edit the LMS settings of your Open edX instance  (*e.g.* ``lms/envs/private.py``) by adding
``fonzie`` to your ``INSTALLED_APPS`` and configure Django Rest Framework (_aka_
DRF) API versioning support as follows:

.. code-block:: python

    # lms/env/private.py
    INSTALLED_APPS += (
        'fonzie',
    )

    # Django Rest Framework (aka DRF)
    REST_FRAMEWORK.update({
        'ALLOWED_VERSIONS': ('1.0', ),
        'DEFAULT_VERSION': '1.0',
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    })


Open edX URLs
^^^^^^^^^^^^^

Add Fonzie's urls in Open edX LMS's URLs:

.. code-block:: python

    # lms/fonzie_urls.py
    from lms.urls import *

    urlpatterns += [
        # [...]
        url(r'^api/', include('fonzie.urls')),
    ]


Test your installation
----------------------

Now that we've installed and configured Fonzie, it's time to test that our API
is responding! If we consider that installed Open edX LMS is served from
``www.mydomain.com`` on the port ``8080``, we can use the ``http`` tool (see `HTTPie
project <https://httpie.org/>`_) to query the API:


.. code-block:: bash

    $ http http://www.mydomain.com:8080/api/v1.0/status/version

    # http command output
    HTTP/1.0 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Language: en
    Content-Type: application/json
    Date: Mon, 28 May 2018 15:37:02 GMT
    Server: WSGIServer/0.1 Python/2.7.12
    Vary: Accept, Accept-Language, Cookie
    X-Frame-Options: ALLOW

    {
        "version": "0.1.0"
    }


Alternatively, you can use ``curl``:


.. code-block:: bash

    $ curl http://www.mydomain.com:8080/api/v1.0/status/version
    {"version":"0.1.0"}


The output of this command should be a JSON payload containing the running
version of Fonzie.
