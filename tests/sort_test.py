import pytest

from main import sort



def test_standard_package():
    assert sort(10, 10, 10, 10) == "STANDARD"

def test_special_package():
    assert sort(100, 100, 100, 10) == "SPECIAL"  
    assert sort(150, 10, 10, 10) == "SPECIAL"    
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_rejected_package():
    assert sort(150, 150, 150, 20) == "REJECTED"
    assert sort(300, 100, 100, 25) == "REJECTED"

def test_edge_cases():
    assert sort(150, 149, 149, 19) == "SPECIAL"
    assert sort(100, 100, 100, 20) == "REJECTED"
    assert sort(99, 99, 99, 10) == "STANDARD"

def test_invalid_inputs():
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 10)
    with pytest.raises(ValueError):
        sort(10, 10, 10, -1)