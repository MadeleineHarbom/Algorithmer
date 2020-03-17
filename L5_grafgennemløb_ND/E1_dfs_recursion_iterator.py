

class dfs_iterator:

    def __init__(self):
        self._graph = None
        self._vistited = []

    def _dfs_visit(self, v):
        self._visited.append(v)
        for edge in v.edges:
            for node in edge.endpoints():
                if node not in self._visited:
                    self._dfs_visit(node)

    def iterator_dfs(self, g, v):
        self._graph = g
        self._visited = []
        self._dfs_visit(v)
        return iter(self._visited)

