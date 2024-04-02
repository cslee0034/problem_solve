graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def recursive_dfs(vertex, discovered=[]):
    discovered.append(vertex)
    for new_vertex in graph[vertex]:
        if (new_vertex) not in discovered:
            discovered = recursive_dfs(new_vertex, discovered)
    return discovered


def iterative_dfs(start_vertex):
    discovered = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()

        if vertex not in discovered:
            discovered.append(vertex)

            for new_vertex in graph[vertex]:
                stack.append(new_vertex)

    return discovered


print(recursive_dfs(1))
print(iterative_dfs(1))
