from typing import Optional
from pydantic import BaseModel


class Node(BaseModel):
    val: int
    neighbors: list[int] = []
    none_or_str: Optional[str] = None


def traverse(node: Node) -> None:
    print(node.val)
    for neighbor in node.neighbors:
        traverse(neighbor)


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            dfs(visited, graph, n)


one = Node(val=1)
two = Node(val=2)
three = Node(val=3)
one.neighbors = [two, three]

graph = {"1": ["2", "3"], "2": [], "3": []}
dfs(set(), graph, "1")

# traverse(one)
