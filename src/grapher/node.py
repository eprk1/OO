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


one = Node(val=1)
two = Node(val=2)
three = Node(val=3)
one.neighbors = [two, three]

traverse(one)
