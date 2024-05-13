# Алгоритм Дейкстры

def find_lowest_cost_node(costs):   # Поиск самого дешёвого пути до узла
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def func(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


graph = {   # Хеш-таблица отношений между узлами
    'start': {'a': 5, 'b': 2},
    'a': {'c': 2, 'd': 2},
    'b': {'a': 8, 'd': 7},
    'c': {'d': 6, 'finish': 3},
    'd': {'finish': 1},
    'finish': {},
}

infinite = float('inf')
costs = {   # Хеш-таблица стоимостей рёбер
    'a': 6,
    'b': 2,
    'c': infinite,
    'd': infinite,
    'finish': infinite
}

parents = {   # Хеш-таблица родителей
    'a': 'start',
    'b': 'start',
    'c': None,
    'd': None,
    'finish': None
}

processed = []   # массив с уже проверенными нодами для find_lowest_cost_node()

func(graph, costs, parents)

print(costs['finish'])
print(parents['finish'])
print(parents['d'])
print(parents['a'])