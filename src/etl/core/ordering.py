from collections import deque
from collections.abc import Collection, Mapping


def topo_sort(nodes: Collection[str], edges: Mapping[str, set[str]])  -> list[str]:
    indeg = {n: 0 for n in nodes}
    for src, dsts in edges.items():
        for d in dsts:
            indeg[d] += 1
    q = deque([n for n in nodes if indeg[n] == 0])
    order = []
    while q:
        n = q.popleft()
        order.append(n)
        for d in edges.get(n, ()):
            indeg[d] -= 1
            if indeg[d] == 0:
                q.append(d)
    if len(order) != len(nodes):
        raise ValueError("Cyclic column dependencies detected")
    return order
