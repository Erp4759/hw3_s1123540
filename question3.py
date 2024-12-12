'''
  Erik Paperniuk
  s1123540
  12.12.2024
'''


def dfs(adj):    # deeep...
    visited, res = [False] * len(adj), []
    def dfs(vertex):
        visited[vertex] = True
        res.append(vertex)
        for neighbour in adj[vertex]:
            if not visited[neighbour]:
                dfs(neighbour)
    dfs(0)
    return res

adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
print(dfs(adj))
