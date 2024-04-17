def bfs(graph, start, n):
    visited = [False] * n
    visited[start] = True
    queue = [start]
    queue_start = 0

    while queue_start < len(queue):
        vertex = queue[queue_start]
        queue_start += 1
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    return visited


def find_root_vertex(graph, n):
    for vertex in range(n):
        visited = bfs(graph, vertex, n)
        if all(visited):
            return vertex
    return -1


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        n = int(file.readline())
        edges = [tuple(map(int, line.split())) for line in file]

    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])

    root = find_root_vertex(graph, n)

    with open('output.txt', 'w') as file:
        if root != -1:
            file.write(f'Root Vertex: {root}')
        else:
            file.write('RootVertex None')
