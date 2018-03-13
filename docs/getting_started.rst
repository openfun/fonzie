Getting Started
===============

Fonzie is supposed to be installed as a Django application running in an Open
edX platform instance. Fonzie has been designed to be integrated with the
current Open edX release (Ginkgo at the time of writing). We plan to support the
next Open edX release (Hawthorn) in a near future.

Pre-requisites for Fonzie contributors
--------------------------------------

We extensively use `Docker <https://docs.docker.com/install/>`_ (17.12+) and
`Docker compose <https://docs.docker.com/compose/install/>`_ (1.18+) in our
development workflow. So, if you intend to work on Fonzie, please, make sure they
are both installed and functionnal before pursuing this installation.

Install dependencies
--------------------

To install Fonzie in an Open edX project, two choices are offered depending on
the way you are running your instance. If Open edX runs as a suite of Docker
containers, Fonzie's development environment can serve as an example of how to
integrate a Django application in `fun-platform
<https://github.com/openfun/fun-platform>`_'s docker stack. Alternatively, if
you are running Open edX on a bare metal server (or virtual machine), the
installation protocol follows a standard Django procedure that will be described
below.

Standard procedure
^^^^^^^^^^^^^^^^^^

Install fonzie and its dependencies in your Open edX installation with ``pip``:

.. code-block:: bash

    $ (sudo) pip install fonzie

Docker procedure
^^^^^^^^^^^^^^^^

TODO

Configure Fonzie
----------------

Once installed, Fonzie needs to be configured as a standard Django application,
_i.e._ adding ``fonzie`` to your ``INSTALLED_APPS`` and Fonzie's URLs to your
project's URLs. Achieving those two steps depends on the way you are running
Open edX.

Standard procedure
^^^^^^^^^^^^^^^^^^

Edit the LMS settings of your Open edX instance  (_e.g._ ``lms/envs/private.py``) by adding
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

And finally, add Fonzie urls in Open edX LMS's URLs:

.. code-block:: python

    # lms/urls.py
    urlpatterns = [
        # [...]
        url(r'^api/', include('fonzie.urls')),
    ]

Docker procedure
^^^^^^^^^^^^^^^^

TODO
