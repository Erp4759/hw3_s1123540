from collections import deque

'''
  Erik Paperniuk
  s1123540
  12.12.2024
'''


def bfs(adj):    #Bread...first search... I am hungry
    visited, traversal = [False] * len(adj), []
    visited[0] = True
    queue = deque([0])
    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)
        for neighbour in adj[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    return traversal

adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(bfs(adj))