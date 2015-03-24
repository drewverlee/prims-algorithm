"""
prims alg on a file with nodes and edges
"""
from prims import prims
from que import SimpleQue as Que
from file_io import file_to_graph

def main():
    """computes prims alg on a file containing nodes edges to find mst
    :returns: cost
    """
    graph = Graph('edges.txt')
    que = Que()
    mst = prims(graph, que)
    return mst.cost
