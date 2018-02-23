Getting Started
===============

If you have not already done so, create/activate a `virtualenv`_. Unless otherwise stated, assume all terminal code
below is executed within the virtualenv.

.. _virtualenv: https://virtualenvwrapper.readthedocs.org/en/latest/


Pre-requisites
--------------

We are using `Dredd <http://dredd.readthedocs.io/en/latest/>`_ to test our API
implementation. It requires `Node.js <https://nodejs.org/en/>`_ to run and we
are using `Yarn <https://yarnpkg.com/en/>`_ to install it. So make sure both
``node`` and ``yarn`` are installed and functionnal before pursuing this
installation.

Install dependencies
--------------------

Dependencies can be installed via `pip` in your project's virtual environment:

.. code-block:: bash

    (venv) $ pip install fonzie

Alternatively, if you indend to work on this project, clone the repository first and then
install requirements _via_ the command below:

.. code-block:: bash

    $ git clone git@github.com:openfun/fonzie.git
    (venv) $ make requirements

Configure Fonzie
----------------

Edit the settings of your project  (_e.g._ ``my_project/settings.py``) by adding
``fonzie`` to your ``INSTALLED_APPS`` and configure Django Rest Framework (_aka_
DRF) API versioning support as follows:

.. code-block:: python

    # my_project/settings.py

    INSTALLED_APPS = (
        # [...]
        'fonzie',
    )

    # Django Rest Framework (aka DRF)
    REST_FRAMEWORK = {
        'ALLOWED_VERSIONS': ('1.0', ),
        'DEFAULT_VERSION': '1.0',
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    }

And finally, configure Fonzie urls for your project:

.. code-block:: python

    # my_project/urls.py
    urlpatterns = [
        # [...]
        url(r'^api/', include('fonzie.urls')),
    ]
