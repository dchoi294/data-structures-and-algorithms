class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.vertices = []

    def add_node(self, value):
        vertex = Vertex(value)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise KeyError("One or both vertices are not part of this graph.")
        edge = Edge(vertex2, weight)
        vertex1.edges.append(edge)

    def get_nodes(self):
        return self.vertices

    def get_neighbors(self, vertex):
        return vertex.edges

    def size(self):
        return len(self.vertices)
