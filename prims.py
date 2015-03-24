"""
prims algorithm provides find's a Minimal Spanning tree
"""
from mst import MST
from pprint import pprint as pp

def prims(graph, que, start_vertice):
    """
    :graph: graph of all vertices and edges
    :start_vertice: dic: vertice and its neighbors
    :que: finds the cheapest spanning edge
    :returns: Minimal Spanning Tree
    """
    mst = MST(vertices=start_vertice)
    while mst.vertices != graph.vertices:
        vertice, neighbors, edge, edge_cost = que.cheapest_spanning_edge(mst, graph)
        mst.vertices[vertice] = neighbors
        mst.edges[edge] = edge_cost
        mst.cost += edge_cost
        mst.path.append(edge)
    return mst






