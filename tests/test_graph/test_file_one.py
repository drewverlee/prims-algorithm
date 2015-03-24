"""
4 4
1 2 1
2 3 2
3 4 3
4 1 4
"""
from graph import Graph



def test_graph_should_be_graph(GF1):
    assert isinstance(GF1, Graph)

def test_graph_should_have_4_vertices(GF1):
    assert len(GF1.vertices) == 4

def test_graph_should_have_4_edges(GF1):
    assert len(GF1.edges) == 4

def test_graph_should_have_vertice_2(GF1):
    assert 2 in GF1.vertices

def test_graph_should_have_edge_2_3(GF1):
    assert frozenset([2, 3]) in GF1.edges

def test_graph_edge_4_1_should_be_4(GF1):
    assert GF1.edges[frozenset([4, 1])] == 4
