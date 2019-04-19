"""
Fonzie, A FUN API for Open edX.
"""
from __future__ import absolute_import, unicode_literals

from os import path

import pkg_resources
from setuptools.config import read_configuration


def _extract_version(package_name):
    """
    Extract fonzie version.

    Get package version from installed distribution or configuration file if not installed
    """
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        _conf = read_configuration(
            path.join(path.dirname(path.dirname(__file__)), "setup.cfg")
        )
    return _conf["metadata"]["version"]


__version__ = _extract_version("fonzie")

default_app_config = "fonzie.apps.FonzieConfig"  # pylint: disable=invalid-name
