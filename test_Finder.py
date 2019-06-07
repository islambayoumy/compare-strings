import pytest
import time

from Finder import Finder
from List_Generator import Generator


@pytest.fixture
def str_list_long_length(request):
    gen = Generator(10000, 100)
    return gen.generate_list()


@pytest.fixture
def str_list_long_size(request):
    gen = Generator(100, 10000)
    return gen.generate_list()


@pytest.fixture
def str_list_large(request):
    gen = Generator(1000, 5000)
    return gen.generate_list()


@pytest.fixture
def str_list_empty_list(request):
    gen = Generator(10, 0)
    return gen.generate_list()


@pytest.fixture
def finder(request):
    return Finder([])


def test_compare_not_equal(finder):
    assert True == finder.compare_str('abc', 'abc')


def test_compare_not_equal(finder):
    assert False == finder.compare_str('aaa', 'aad')


def test_find_long_string_length_not_empty(str_list_long_length):
    finder = Finder(str_list_long_length)
    result = finder.find(str_list_long_length[50])
    assert len(result) > 0


def test_find_long_list_size_not_empty(str_list_long_size):
    finder = Finder(str_list_long_size)
    result = finder.find(str_list_long_size[50])
    assert len(result) > 0


def test_find_large_not_empty(str_list_large):
    finder = Finder(str_list_large)
    result = finder.find(str_list_large[100])
    assert len(result) > 0


def test_find_empty_list(str_list_empty_list):
    finder = Finder(str_list_empty_list)
    result = finder.find('abd')
    assert not len(result)


def test_execution_time_for_large_input(str_list_large):
    finder = Finder(str_list_large)
    start_time = time.time()
    finder.find(str_list_large[100])
    assert (time.time() - start_time) < 10
