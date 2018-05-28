Developer guide
===============

Fonzie's project has been designed with "container-native development" in mind.
In this guide, we will consider that your are familiar with Docker and its
ecosystem.


Pre-requisites for Fonzie contributors
--------------------------------------

As you might already have expected, we extensively use `Docker
<https://docs.docker.com/install/>`_ (17.12+) and `Docker compose
<https://docs.docker.com/compose/install/>`_ (1.18+) in our development
workflow. So, if you intend to work on Fonzie, please, make sure they are both
installed and functional before pursuing this guide.


Getting started with the development stack
------------------------------------------

First things first, to start contributing on the project, you will need to clone
Fonzie's repository and then build the Docker-based development stack with:

.. code-block:: bash

    # Clone Fonzie's repository
    $ git clone git@github.com:openfun/fonzie.git

    # Build required containers
    $ make bootstrap


The ``make bootstrap`` command will:

- build an ``edx-platform`` Docker image with Fonzie installed and configured,
- install node dependencies (``dredd``, etc.),
- perform Open edx LMS database migrations.

Now you should be able to start the development server via:

.. code-block:: bash

    $ make run


Fonzie's API should be accessible from:
`http://localhost:8072/api/v1.0/
<http://localhost:8072/api/v1.0/>`_

We invite you to test the ``status/version`` endpoint to ensure everything went
well:

.. code-block:: bash

    $ curl http://www.mydomain.com:8080/api/v1.0/status/version
    {"version":"0.1.0"}


Development workflow
--------------------

If you use to work with Django's development server, you will have the same
experience with a Docker-based development stack: Fonzie is installed in edit
mode and mounted as a volume in the ``lms`` service. Combined with the
development server, the application will be reloaded when the source code
changes.

Adding dependencies
-------------------

If your work on Fonzie requires new dependencies, you will need to:

1. Update the ``options.install_requires`` section of the ``setup.cfg`` file (or
   the ``options.extras_require.[dev,doc,...]`` section if it's a development
   dependency),
2. Rebuild the ``lms`` service image via the ``make build`` utility.
3. Optionally perform required database migrations via:

.. code-block:: bash

    $ bin/run lms python manage.py lms migrate
