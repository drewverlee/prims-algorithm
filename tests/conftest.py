import pytest
from graph import Graph
from que import SimpleQue
import mocks

@pytest.fixture()
def GF1():
    return Graph('data/one.txt')

@pytest.fixture()
def GF2():
    return Graph('data/two.txt')

@pytest.fixture()
def simple_que():
    return SimpleQue()

@pytest.fixture()
def mock_abcd():
    return mocks.abcd



