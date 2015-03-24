from collections import defaultdict

class MST(object):

    """Minimal Spanning Tree"""

    def __init__(self, vertices, edges={}, cost=0):
        """TODO: to be defined1.

        :vertices: TODO
        :edges: TODO

        """
        self.vertices = defaultdict(list)
        self.vertices.update(vertices)
        self.edges = defaultdict(float)
        self.edges.update(edges)
        self.cost = cost
        self.path = []

    def cost_path(self):
        return [self.edges[edge] for edge in self.path]

        
