#long document is long


class DiectedVertex:

    def __init__(self, e):
        self._element = e
        self._edges = []

    def __str__(self):
        return str(self._element)

    def element(self):
        return self._element

    def edges(self):
        return self._edges


class FlowEdge:
    def __init__(self, e, startVertex, endVertex,capacity):
        self._element = e
        self._startpoint = startVertex
        self._endpoint = endVertex
        self._flow = 0
        self._capacity = capacity
        startVertex.edges.append(self)


    def __str__(self):
        return str(self._element)

    def element(self):
        return self._element

    def endpoint(self):
        return self._endpoint

    def startpoint(self):
        return self._startpoint

    def flow(self):
        return self._flow

    def capacity(self):
        return self._capacity

    def unused_capacity(self):
        return self._capacity - self._flow

    def add_flow(self, flow):
        self._flow = self._flow + flow

class FlowGraph:

    def __init__(self):
        self._vertices = []
        self._edges = []

    # Inserts and returns a new vertex containing the element e.
    # Input: V; Output: Vertex
    def insert_vertex(self, e):
        v = DiectedVertex(e)
        self._vertices.append(v)
        return v

    # Removes the vertex v and all its incident edges
    # Input: Vertex; Output: nothing
    def remove_vertex(self, v):
        for e in self._edges:
            if e._startpoint == v or e._endpoint == v:
                self.remove_edge(e)
    # Inserts and returns a new edge between the vertices v and w.
    # The element of the edge is o.
    def insert_edge(self, name, startVertex, endVertex, capacity):
        e = FlowEdge(name, startVertex, endVertex, capacity)
        startVertex.edges.append(e)
        self._edges.append(e)
        return e

    # Removes the edge e.
    # Input: Edge; Output: nothing
    def remove_edge(self, e):
        e.startpoint().edges.remove(e)
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



    # Returns whether the vertices v and w are adjacent.
    # Input: Vertex, Vertex; Output: boolean
    def are_adjacent(self, v, w):
        for e in v.edges:
            if e._endpoint() == w:
                return True
        for f in w.edges:
            if f._endpoint() == v:
                return False


    def print_graph(self, start):
        printed_v = []
        queue = []
        print('v: ' + start.element())
        printed_v.append(start)
        for edge in start.edges():
            queue.append(edge.endpoint())
        counter = 0
        while counter < len(queue):
            current = queue[len(queue)-1]
            for edge in current:
                print('Edge capacity:' + edge.capacity() + '. Flow: ' + edge.flow() +
                      '. Residual: ' + edge.unused_capacity())
                if edge.endpoint() not in printed_v or edge.endpoint() not in queue:
                    queue.append(edge.endpoint())



