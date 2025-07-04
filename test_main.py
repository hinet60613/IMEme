import pytest
from main import Alignment

def test_alignment():
    assert Alignment.TOP.value == 'top'
