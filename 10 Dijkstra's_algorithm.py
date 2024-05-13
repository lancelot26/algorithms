# Алгоритм Дейкстры
processed = 1
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost:
            #and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def func(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]


graph = {
    'start': {'a': 2, 'b': 5},
    'a': {'finish': 1},
    'b': {'a': 3, 'finish': 5},
    'finish': {}
}

