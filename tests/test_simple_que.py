from que import SimpleQue
from mocks import A_B, B, A_B_COST


def test_simple_que_should_be_simple_que(simple_que):
    assert isinstance(simple_que, SimpleQue)


def test_simple_que_should_find_cheapest_spanning_egde(simple_que, mock_abcd):
    vertice_not_in_mst, _, _ = \
        simple_que.cheapest_spanning_edge(mock_abcd.mst_start, mock_abcd.graph)
    assert vertice_not_in_mst == B

def test_simple_que_should_find_cheapest_spanning_vertice(simple_que, mock_abcd):
    _, min_edge, _ = \
        simple_que.cheapest_spanning_edge(mock_abcd.mst_start, mock_abcd.graph)
    assert min_edge == A_B

def test_simple_que_should_find_cheapest_spanning_egde_cost(simple_que, mock_abcd):
    _, _, edge_cost = \
        simple_que.cheapest_spanning_edge(mock_abcd.mst_start, mock_abcd.graph)
    assert edge_cost == A_B_COST





