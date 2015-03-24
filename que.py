"""
contains ques used to find the cheapest edge
"""


class SimpleQue(object):

    """simple que just search its all!"""

    def __init__(self):
        """TODO: to be defined1. """

    def cheapest_spanning_edge(self, mst, graph):
        """find the cheapest spanning edge

        mst: minimal spanning tree
        graph: graph

        Returns: tuple: (num, num, num): vertice (not in mst yet), edge and 
            edge cost

        """
        min_edge_cost = float('inf')
        vertice_not_in_mst = None
        min_edge = None
        for mst_vertice in mst.vertices:
            for neighbor in graph.neighbors[mst_vertice]:
                if neighbor not in mst.vertices:
                    edge = frozenset([mst_vertice, neighbor])
                    edge_cost = graph.edges[edge]
                    if edge_cost < min_edge_cost:
                        vertice_not_in_mst = neighbor
                        min_edge_cost = edge_cost
                        min_edge = edge
        return vertice_not_in_mst, min_edge, min_edge_cost
