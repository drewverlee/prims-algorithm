from prims import prims

def test_prims_should_find_cost_of_neg_16(GF4, simple_que):
    v = GF4.any_vertice()
    mst = prims(GF4, simple_que, v)
    assert mst.cost == 1.81
