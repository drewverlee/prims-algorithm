import pytest
from graph import Graph
from que import SimpleQue
import mocks

# ======= Graphs ==========
@pytest.fixture(scope="module")
def GF1():
    return Graph('data/one.txt')

@pytest.fixture(scope="module")
def GF2():
    return Graph('data/two.txt')

@pytest.fixture(scope="module")
def GF3():
    return Graph('data/three.txt')

@pytest.fixture(scope="module")
def GF4():
    return Graph('data/four.txt')

# ======= ques ============
@pytest.fixture(scope="module")
def simple_que():
    return SimpleQue()


# ======= mock ============
@pytest.fixture(scope="module")
def mock_abcd():
    return mocks.abcd()

@pytest.fixture(scope="function")
def mock_simple_que():
    return mocks.simple_que()

@pytest.fixture(scope="module")
def A():
    return {1: {2, 3}} # hacks 







