from utils import arrs

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_get_non_existing_index():
    assert arrs.get([1, 2, 3], 5, "test") == "test"

def test_get_empty_array():
    assert arrs.get([], 0, "test") == "test"
def test_my_slice_default():
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_my_slice_with_start():
    assert arrs.my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]

def test_my_slice_with_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], end=3) == [1, 2, 3]

def test_my_slice_with_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]

def test_my_slice_negative_start():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]

def test_my_slice_negative_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], end=-2) == [1, 2, 3]

def test_my_slice_negative_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]