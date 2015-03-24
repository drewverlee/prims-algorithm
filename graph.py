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
        vertices = defaultdict(set)
        edges = defaultdict(float)

        with open(a_file) as f:
            # skip header
            next(f)
            for line in f:
                u, v, cost = [float(i) for i in line.split()]
                vertices[u].add(v)
                vertices[v].add(u)
                edge = frozenset([u,v])
                edges[edge] = cost
        return vertices, edges

    def any_vertice(self):
        """return any vertice and its neighbors"""
        # the list is sorted ascending 1, 2, 3... so this 
        # always returns the lowest number
        v = list(self.vertices)[0]
        return {v: self.vertices[v]}



            
