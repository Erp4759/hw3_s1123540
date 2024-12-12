'''
  Erik Paperniuk
  s1123540
  12.12.2024
'''


def make_graph(nodes, edges):  #it's like what google maps use for finding routes
    graph = [[] for _ in range(nodes)]
    for edge in edges:
        x, y = edge
        graph[x].append(y)
        graph[y].append(x)
    for neighbours in graph:
        neighbours.sort()
    return graph

nodes = 5
E = 5
edges = [[0, 1], [0, 4], [4, 1], [4, 3], [1, 3], [1, 2], [3, 2]]

print(make_graph(nodes, edges))