'''error path tests for 6 degress of kb'''
import sys
import pytest
sys.path.insert(0, "..")

from degrees_of_kb import KevinBacon6Degrees
import pytest

def test_invalid_url():
    '''test a valid url and that urls is populated'''
    k_b = KevinBacon6Degrees("/nonesense!/Kevin_Bacon")
    with pytest.raises(ValueError):
        k_b.generate_6_degrees()


def test_empty_url():
    '''test empty url'''
    with pytest.raises(ValueError):
        k_b = KevinBacon6Degrees("")\
            


def test_no_url():
    ''' test no url'''
    with pytest.raises(ValueError):
        k_b = KevinBacon6Degrees(None)\
    
