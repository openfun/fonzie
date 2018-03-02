Fonzie, a FUN API for Open edX
==============================

|pypi-badge| |travis-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge|

**This project is in early-development phase, we are still experimenting on
it.** It is intended to be community-driven, so please, do not hesitate to get
in touch if you have any question related to our implementation or design
decisions.

Overview
--------

Fonzie is an HTTP API over the `Open edX <https://open.edx.org/>`_ project. It
has been build to open the way to new tools and interfaces in the Open edX
ecosystem.

We choose to design the API first and then propose an implementation with
Fonzie. The current state of the API schema is available in `API blueprint
format <https://github.com/openfun/fonzie/blob/master/fonzie-v1-0.apib>`_; it
can be used to start developing a front-end application that will consume
Fonzie's API (take a look at `API blueprint tools
<https://apiblueprint.org/tools.html>`_).

Documentation
-------------

The full documentation is at https://fonzie.readthedocs.org.

License
-------

The code in this repository is licensed under the AGPL 3.0 unless otherwise
noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for Open edX code in general.

PR description template should be automatically applied if you are sending PR
from github interface; otherwise you can find it it at `PULL_REQUEST_TEMPLATE.md
<https://github.com/openfun/fonzie/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_

Issue report template should be automatically applied if you are sending it from
github UI as well; otherwise you can find it at `ISSUE_TEMPLATE.md
<https://github.com/openfun/fonzie/blob/master/.github/ISSUE_TEMPLATE.md>`_

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@fun-mooc.fr.

Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help


.. |pypi-badge| image:: https://img.shields.io/pypi/v/fonzie.svg
    :target: https://pypi.python.org/pypi/fonzie/
    :alt: PyPI

.. |travis-badge| image:: https://travis-ci.org/openfun/fonzie.svg?branch=master
    :target: https://travis-ci.org/openfun/fonzie
    :alt: Travis

.. |codecov-badge| image:: http://codecov.io/gh/openfun/fonzie/coverage.svg?branch=master
    :target: http://codecov.io/gh/openfun/fonzie?branch=master
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/fonzie/badge/?version=latest
    :target: http://fonzie.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/fonzie.svg
    :target: https://pypi.python.org/pypi/fonzie/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/openfun/fonzie.svg
    :target: https://github.com/openfun/fonzie/blob/master/LICENSE.txt
    :alt: License
