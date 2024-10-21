from typing import TypeVar, Generic, List

__all__ = ("Node", "Graph")

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value
        self.outbound: List[Node[T]] = []
        self.inbound: List[Node[T]] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node[T]") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__

class Graph(Generic[T]):
    def __init__(self, root: Node[T]) -> None:
        self._root = root

    def dfs(self) -> List[Node[T]]:
        visited = set()
        result = []

        def _dfs(node: Node[T]) -> None:
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            for neighbor in node.outbound:
                _dfs(neighbor)

        _dfs(self._root)
        return result

    def bfs(self) -> List[Node[T]]:
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
