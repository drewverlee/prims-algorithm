from collections import namedtuple, defaultdict
from mock import MagicMock

# ABCD SQUARE GRAPH
# ==============================
ABCD = namedtuple("ABCD", ["graph", "mst_final", "mst_start"])

# obviously this isnt great, i need to think about how to set up mock objects
# better
A = 1
B = 2
C = 3
D = 4
A_B = frozenset([A, B]) 
A_C = frozenset([A, C]) 
B_D = frozenset([B, D]) 
C_D = frozenset([C, D]) 
A_B_COST = 0
A_C_COST = 1
B_D_COST = 10
C_D_COST = 100

def abcd():

    abcd_square_graph_layout = \
    """
    A/1     0     B/2
    +-------+  
    |       |  
    |       | 10
  1 |       |  
    +-------+  
        100    
    C/3         D/4
    """




    abcd_vertices = set([A, B, C, D])
    abcd_vertices_w_neighbors = \
        {A: {B, C}, 
        B: {A, D},
        C: {A, D},
        D: {B, C}
        }

    abcd_edges = {
            A_B: A_B_COST,
            A_C: A_C_COST,
            B_D: B_D_COST,
            C_D: C_D_COST,
            }
    abcd_square_graph = MagicMock()
    abcd_square_graph.edges = abcd_edges
    abcd_square_graph.vertices = abcd_vertices_w_neighbors 
    abcd_square_graph.layout = abcd_square_graph_layout


    # ABCD MST Final
    #===================
    ABCD_square_mst_layout = \
    """
    A     0       B  
    +---------+    
    |         |    
    |         |    
  1 |         |  10
    |         |    
    +         +    
    C                D
    """
    # remove edge
    # MST final
    abcd_edges.pop(C_D) 
    abcd_square_mst_final = MagicMock()
    abcd_square_mst_final.vertices = abcd_vertices_w_neighbors
    abcd_square_mst_final.edges = abcd_edges
    abcd_square_mst_final.layout = ABCD_square_mst_layout
    abcd_square_mst_final.cost = 11

    # ABCD MST START

    abcd_square_mst_start = MagicMock()
    abcd_square_mst_start.vertices = set([A])
    abcd_square_mst_start.edges = defaultdict(float)
    abcd_square_mst_start.layout = "A"

    abcd = ABCD(graph=abcd_square_graph, 
            mst_final=abcd_square_mst_final, 
            mst_start=abcd_square_mst_start)
    return abcd

# ===== mock que ==========
def simple_que():
    simple_que = MagicMock()
    simple_que.i = -1
    values = [
            (B, {A, D}, A_B, A_B_COST),
            (C, {A, D}, A_C,  A_C_COST),
            (D, {C, B}, B_D, B_D_COST)
            ]
    def side_effect(*args):
        simple_que.i +=1
        return values[simple_que.i]

    simple_que.cheapest_spanning_edge = side_effect
    return simple_que

