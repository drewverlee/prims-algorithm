"""
4 5
1 2 1
1 4 4
2 3 2
2 4 1
3 4 3
"""
from graph import Graph


def test_graph_should_be_graph(GF2):
    assert isinstance(GF2, Graph)

def test_graph_should_have_4_vertices(GF2):
    assert len(GF2.vertices) == 4

def test_graph_should_have_4_edges(GF2):
    assert len(GF2.edges) == 5

def test_graph_should_have_vertice_2(GF2):
    assert 2 in GF2.vertices

def test_graph_should_have_edge_2_3(GF2):
    assert frozenset([2, 3]) in GF2.edges

def test_graph_edge_4_1_should_be_4(GF2):
    assert GF2.edges[frozenset([4, 1])] == 4


    



