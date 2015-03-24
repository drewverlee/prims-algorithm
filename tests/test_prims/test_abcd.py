from prims import prims


def test_should_find_cost_of_11(mock_abcd, mock_simple_que, A):
    outcome_mst = prims(mock_abcd.graph, mock_simple_que, A)
    outcome_cost = outcome_mst.cost
    expected_cost = mock_abcd.mst_final.cost
    assert outcome_cost == expected_cost

def test_should_find_vertices_A_B_C_D(mock_abcd, mock_simple_que, A):
    outcome_mst = prims(mock_abcd.graph, mock_simple_que, A)
    outcome_vertices = outcome_mst.vertices
    expected_vertices = mock_abcd.mst_final.vertices
    assert outcome_vertices == expected_vertices

def test_should_find_edges(mock_abcd, mock_simple_que, A):
    outcome_mst = prims(mock_abcd.graph, mock_simple_que, A)
    outcome_edges = outcome_mst.edges
    expected_edges = mock_abcd.mst_final.edges
    assert outcome_edges == expected_edges
