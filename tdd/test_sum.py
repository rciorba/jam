import pytest


# def split(string):
#     acc = []
#     pass_1 = string.split(",")
#     for item in pass_1:
#         numbers = item.split('\n')
#         acc.extend(numbers)
#     return acc


class SumException(Exception):
    pass


def split(string, delimiter):
    string = string.replace("\n", delimiter)
    return string.split(delimiter)


def extract_delim(string):
    delim = ","
    if string.startswith("//"):
        delim, string = string.split("\n", 1)
        delim = delim[2:]
    return delim, string

def add(numbers):
    numbers = numbers.strip()
    delim, numbers = extract_delim(numbers)
    if numbers == "":
        return 0
    numbers = split(numbers, delim)
    numbers = [int(n) for n in numbers]
    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise SumException(str(negatives))
    return sum(numbers)


def test_empty_string():
    assert add("") == 0


def test_one_number():
    assert add("4") == 4


def test_two_numbers():
    assert add("4, 7") == 11


def test_negative_numbers():
    with pytest.raises(SumException) as exception:
        assert add("4, -7, 8 , -9") == 11
    assert str(exception.value) == "[-7, -9]"


def test_muptiple_numbers():
    assert add("3, 7, 10, 12, 2") == 34


def test_newline_comma():
    assert add("3, 7, 10, 12\n2") == 34


def test_special_delimitter():
    assert add("//;\n3; 7; 10; 12;2") == 34


def test_extract_delimitter():
    assert extract_delim("//;\n3; 7; 10; 12;2") == (";", "3; 7; 10; 12;2")


def test_sum():
    assert 1+1 == 2
