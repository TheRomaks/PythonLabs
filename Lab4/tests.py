import pytest
from string import ascii_lowercase, ascii_uppercase
from tasks.abrange import generate_abs_numbers
from tasks.multiply import multiply_lists
from tasks.passwd import generate_passwords


def test_generate_abs_numbers_positive_range():
    a = 1
    b = 5
    generator = generate_abs_numbers(a, b)
    expected = [1, 2, 3, 4, 5]
    assert list(generator) == expected

def test_generate_abs_numbers_negative_range():
    a = -5
    b = 1
    generator = generate_abs_numbers(a, b)
    expected = [5, 4, 3, 2, 1, 0, 1]
    assert list(generator) == expected

def test_generate_passwords_valid_length():
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    length = 10
    generator = generate_passwords(chars, length)
    for i in range(5):
        password = next(generator)
        assert len(password) == length
        assert all(char in chars for char in password)

def test_generate_passwords_invalid_length():
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    length = 0
    with pytest.raises(ValueError):
        list(generate_passwords(chars, length))

def test_multiply():
    list1=[1,2,3]
    list2=[3,2,1]
    result= multiply_lists(list1,list2)
    res_test=[3,4,3]
    assert list(result) == res_test

def test_multiply2():
    list1 = [3, 3, 3]
    list2 = [3, 3, 3]
    result = multiply_lists(list1, list2)
    res_test = [9, 9, 9]
    assert list(result) == res_test
