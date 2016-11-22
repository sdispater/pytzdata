# -*- coding: utf-8 -*-

import os
import pytest

from pytzdata import tz_file, set_directory
from pytzdata.exceptions import TimezoneNotFound


def setup_module(module):
    if 'PYTZDATA_TZDATADIR' in os.environ:
        del os.environ['PYTZDATA_TZDATADIR']

    set_directory()


def teardown_module(module):
    if 'PYTZDATA_TZDATADIR' in os.environ:
        del os.environ['PYTZDATA_TZDATADIR']

    set_directory()


def test_tz_file():
    here = os.path.realpath(os.path.dirname(__file__))
    filepath = os.path.realpath(
        os.path.join(here, '..', 'pytzdata', 'zoneinfo', 'Europe', 'Paris')
    )

    with open(filepath) as f1:
        with tz_file('Europe/Paris') as f2:
            assert f1.name == f2.name

def test_tz_file_not_found():
    with pytest.raises(TimezoneNotFound):
        tz_file('Invalid')

def test_tz_file_invalid_name():
    with pytest.raises(ValueError):
        tz_file('Europe/../Paris')
