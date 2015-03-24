"""
4 4
1 2 1
2 3 2
3 4 3
4 1 4
"""
from prims import prims

def test_prims_should_find_cost_of_6(GF1, simple_que):
    v = GF1.any_vertice()
    mst = prims(GF1, simple_que, v)
    assert mst.cost == 6

def test_prims_should_find_vertices_1_2_3(GF1, simple_que):
    v = GF1.any_vertice()
    mst = prims(GF1, simple_que, v)
    assert mst.vertices.keys() == {1, 2, 3, 4}

def test_prims_should_find_edges(GF1, simple_que):
    v = GF1.any_vertice()
    mst = prims(GF1, simple_que, v)
    assert mst.edges.keys() == {
            frozenset([1, 2]),
            frozenset([2, 3]),
            frozenset([3, 4]),
            }

def test_prims_should_find_path(GF1, simple_que):
    v = GF1.any_vertice()
    mst = prims(GF1, simple_que, v)
    assert mst.cost_path() == [1, 2, 3]
