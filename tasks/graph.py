from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = set()
        result = []

        def _dfs(node: Node):
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            for neighbor in node.outbound:
                _dfs(neighbor)

        _dfs(self._root)
        return result

    def bfs(self) -> list[Node]:
        visited = set()
        queue = [self._root]
        result = []

        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            result.append(node)
            for neighbor in node.outbound:
                if neighbor not in visited:
                    queue.append(neighbor)

        return result
