'''happy path tests for 6 degress of kb'''
import sys
import pytest
sys.path.insert(0, "..")
from degrees_of_kb import KevinBacon6Degrees

def test_valid_url():
    '''test a valid url and that urls is populated'''
    k_b = KevinBacon6Degrees("/wiki/Kevin_Bacon")
    k_b.generate_6_degrees()
    assert len(k_b.urls) == 6
