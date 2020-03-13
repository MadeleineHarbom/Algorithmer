#long document is long


class Vertex:

    def __init__(self, e):
        self._element = e
        self.edges = []

    def __str__(self):
        return str(self._element)

    def element(self):
        return self._element


class Edge:
    def __init__(self, e, v1, v2):
        self._element = e
        self._endpoints = [v1, v2]
        v1.edges.append(self)
        v2.edges.append(self)

    def __str__(self):
        return str(self._element)

    def element(self):
        return self._element

    def endpoints(self):
        return self._endpoints


class Graph:

    def __init__(self):
        self._vertices = []
        self._edges = []

    # Inserts and returns a new vertex containing the element e.
    # Input: V; Output: Vertex
    def insert_vertex(self, e):
        v = Vertex(e)
        self._vertices.append(v)
        return v

    # Removes the vertex v and all its incident edges
    # Input: Vertex; Output: nothing
    def remove_vertex(self, v):
        for e in v.edges:
            self.remove_edge(e)

    # Inserts and returns a new edge between the vertices v and w.
    # The element of the edge is o.
    def insert_edge(self, o, v, w):
        e = Edge(o, v, w)
        self._edges.append(e)
        return e

    # Removes the edge e.
    # Input: Edge; Output: nothing
    def remove_edge(self, e):
        for v in e.endpoints():
            v.edges.remove(e)
        self._edges.remove(e)

    # Returns the count of vertices in the graph.
    # Input: nothing; Output: int
    def num_vertices(self):
        return len(self._vertices)

    # Returns the count of edges in the graph.
    # Input: nothing; Output: int
    def num_edges(self):
        return len(self._edges)

    # Returns an iterator on the vertices in the graph.
    # Input: nothing; Output: Iterator
    def vertices(self):
        return iter(self._vertices)

    # Returns an iterator on the edges in the graph.
    # Input: nothing; Output: Iterator
    def edges(self):
        return iter(self._edges)

    # Returns the degree of the vertex v.
    # Input: Vertex; Output: int
    def degree(self, v):
        return len(v.edges)

    # Returns an iterator on the vertices that are adjacent to v.
    # Input: Vertex; Output: Iterator
    def adjacent_vertices(self, v):
        a = []
        for e in v.edges:
            a.append(e)
        return a

    # Returns an iterator on the edges that are incident to v.
    # Input: Vertex; Output: Iterator
    def incident_edges(self, v):
        return v.edges

    # Returns a list with the two vertices at the ends of the edge e.
    # Input: Edge; Output: list with 2 vertices
    def end_vertices(self, e):
        return e.endpoints()

    # Returns the vertex opposite v along the edge e.
    # Input: Vertex, Edge; Output: Vertex
    def opposite(self, v, e):
        if e.endpoints()[0] == v:
            return e.endpoints()[1]
        else:
            return e.endpoints()[0]

    # Returns whether the vertices v and w are adjacent.
    # Input: Vertex, Vertex; Output: boolean
    def are_adjacent(self, v, w):
        for e in v.edges:
            if e in w.edges:
                return True

        return False

