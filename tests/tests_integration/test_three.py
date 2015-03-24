"""
6 11
1 2 10
1 5 -3
1 4 5
1 3 4
2 6 6
2 3 7
3 6 -10
3 4 -1
4 6 2
4 5 -8
5 6 1
"""
from prims import prims

def test_prims_should_find_cost_of_neg_16(GF3, simple_que):
    v = GF3.any_vertice()
    mst = prims(GF3, simple_que, v)
    assert mst.cost == -16

