from data_structures.graph import Graph


def direct_flights(graph, names):
    if len(names) < 2:
        return False, 0

    nodes = [node for node in graph.nodes if node.value in names]
    for i in range(len(nodes) - 1):
        if nodes[i + 1] not in nodes[i].neighbors:
            return False, 0

    cost = 0
    for i in range(len(nodes) - 1):
        cost += nodes[i].neighbors[nodes[i + 1]]

    return True, cost

