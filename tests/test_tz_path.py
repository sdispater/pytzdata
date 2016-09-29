# -*- coding: utf-8 -*-

import os
import pytest

from pytzdata import tz_path
from pytzdata.exceptions import TimezoneNotFound


def test_tz_path():
    here = os.path.realpath(os.path.dirname(__file__))
    filepath = os.path.realpath(
        os.path.join(here, '..', 'pytzdata', 'zoneinfo', 'Europe', 'Paris')
    )

    assert filepath == tz_path('Europe/Paris')

def test_tz_path_not_found():
    with pytest.raises(TimezoneNotFound):
        tz_path('Invalid')

def test_tz_path_invalid_name():
    with pytest.raises(ValueError):
        tz_path('Europe/../Paris')
