"""
4 5
1 2 1
1 4 4
2 3 2
2 4 1
3 4 3
"""
from prims import prims

def test_prims_should_find_cost_of_4(GF2, simple_que):
    v = GF2.any_vertice()
    mst = prims(GF2, simple_que, v)
    assert mst.cost == 4

def test_prims_should_find_vertices_1_2_3_4(GF2, simple_que):
    v = GF2.any_vertice()
    mst = prims(GF2, simple_que, v)
    assert mst.vertices.keys() == {1, 2, 3, 4}

def test_prims_should_find_edges(GF2, simple_que):
    v = GF2.any_vertice()
    mst = prims(GF2, simple_que, v)
    assert mst.edges.keys() == {
            frozenset([1, 2]),
            frozenset([2, 4]),
            frozenset([2, 3]),
            }

def test_prims_should_find_path(GF2, simple_que):
    v = GF2.any_vertice()
    mst = prims(GF2, simple_que, v)
    assert mst.cost_path() == [1, 1, 2]
