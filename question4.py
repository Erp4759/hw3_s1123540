'''
  Erik Paperniuk
  s1123540
  12.12.2024
'''



def find_leader(parents, node): # finding oue leder from parents
    if parents[node] == node:
        return node
    parents[node] = find_leader(parents, parents[node])
    return parents[node]


def union_sets(parents, ranks, node1, node2): # like Soviet Union
    leader1 = find_leader(parents, node1) # Biden
    leader2 = find_leader(parents, node2) # Trump

    if ranks[leader1] < ranks[leader2]:
        parents[leader1] = leader2
    elif ranks[leader1] > ranks[leader2]:
        parents[leader2] = leader1
    else:
        parents[leader2] = leader1
        ranks[leader1] += 1


def minimum_spanning_tree(num_nodes, edges):  # TRUMP 2024!!!
    edges.sort(key=lambda edge: edge[2])
    parents = [i for i in range(num_nodes)]
    ranks = [0] * num_nodes
    mst_weight = 0
    edge_count = 0

    for edge in edges:
        node1, node2, weight = edge
        leader1 = find_leader(parents, node1) # Biden
        leader2 = find_leader(parents, node2) # Trump

        if leader1 != leader2:
            mst_weight += weight
            edge_count += 1
            union_sets(parents, ranks, leader1, leader2)
            if edge_count == num_nodes - 1:
                break

    return mst_weight


num_towns = 3
roads = [
    [0, 1, 5],
    [1, 2, 3],
    [0, 2, 1]
]

print(minimum_spanning_tree(num_towns, roads))
