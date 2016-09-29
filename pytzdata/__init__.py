# -*- coding: utf-8 -*-

import os

from .exceptions import TimezoneNotFound
from ._compat import FileNotFoundError


def tz_file(name):
    """
    Open a timezone file from the zoneinfo subdir for reading.

    :param name: The name of the timezone.
    :type name: str

    :rtype: file
    """
    try:
        filepath = tz_path(name)

        return open(filepath, 'rb')
    except TimezoneNotFound:
        # http://bugs.launchpad.net/bugs/383171 - we avoid using this
        # unless absolutely necessary to help when a broken version of
        # pkg_resources is installed.
        try:
            from pkg_resources import resource_stream
        except ImportError:
            resource_stream = None

        if resource_stream is not None:
            try:
                return resource_stream(__name__, 'zoneinfo/' + name)
            except FileNotFoundError:
                return tz_path(name)

        raise

def tz_path(name):
    """
    Return the path to a timezone file.

    :param name: The name of the timezone.
    :type name: str

    :rtype: str
    """
    name_parts = name.lstrip('/').split('/')
    for part in name_parts:
        if part == os.path.pardir or os.path.sep in part:
            raise ValueError('Bad path segment: %r' % part)

    filepath = os.path.join(os.path.dirname(__file__),
                            'zoneinfo', *name_parts)

    if not os.path.exists(filepath):
        raise TimezoneNotFound('Timezone {} not found at {}'.format(name, filepath))

    return filepath
