Pendulum
########

.. image:: https://travis-ci.org/sdispater/pytzdata.png
   :alt: Pytzdata Build status
   :target: https://travis-ci.org/sdispater/pytzdata

Official timezone database for Python.

Supports Python **2.7+** and **3.5+**.


Installation
============

    pip install pytzdata


Usage
=====

You can access the content of a specific timezone file by using the `tz_file()` function:

.. code-block:: python

    from pytzdata import tz_file

    with tz_file('Europe/Paris') as f:
        # Do something with the file

If you just want to know the path to a specific timezone file, you may use the `tz_path()` function:

.. code-block:: python

    from pytzdata import tz_path

    tz_path('Europe/Paris')


Release
=======

To make a new release just follow these steps:

- ``make data``
- Update version numbers in ``pytzdata/version.py`` and ``tests/test_version.py``
- ``make tox``


Resources
=========

* `Issue Tracker <https://github.com/sdispater/pytzdata/issues>`_
