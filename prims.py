"""
prims algorithm provides find's a Minimal Spanning tree
"""

def prims(graph, que):
    """finds a Minimal Spanning Tree

    :graph: TODO
    :que: callable that finds the cheapest_edge
    :returns: mst

    """
    mst = MST(vertices = {random(graph.vertice)}, edges=set())
    while mst.vertices != graph.vertices:
        vertice, edge, edge_cost = que.cheapest_spanning_edge(mst, graph)
        mst.vertices.add(vertice)
        mst.edges.add(edge)
        mst.cost += edge_cost
    return mst
        




