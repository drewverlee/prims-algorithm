"""
undirected Graph of vertices and edges
"""
from collections import defaultdict

class Graph(object):

    """undirected Graph of vertices and edges"""

    def __init__(self, a_file):
        """create a undirected graph from a file

        :a_file: location of file

        """
        self._file = a_file
        self.vertices, self.edges, = self._from_file(a_file)

    def _from_file(self, a_file):
        """create vertices and edges from file"""
        vertices = set()
        edges = defaultdict(float)

        with open(a_file) as f:
            # skip header
            next(f)
            for line in f:
                u, v, cost = [float(i) for i in line.split()]
                vertices.add(u)
                vertices.add(v)
                edge = frozenset([u,v])
                edges[edge] = cost
        return vertices, edges



            
