import csv


def read_graph_from_csv(filename):
    """
    Функція зчитування графа з CSV файлу.

    Параметри:
    - filename: рядок, назва CSV файлу

    Повертає:
    Словник, представлення графа.
    """
    graph = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            k1, k2, distance = row
            distance = int(distance)
            if k1 not in graph:
                graph[k1] = {}
            if k2 not in graph:
                graph[k2] = {}
            graph[k1][k2] = distance
            graph[k2][k1] = distance
    return graph


def find_parent(parent, node):
    """
    Функція знаходження представника вершини за допомогою методу об'єднання з рангами.

    Параметри:
    - parent: словник, представлення батьківських вершин
    - node: рядок, вершина графа

    Повертає:
    Представника вершини.
    """
    if parent[node] == node:
        return node
    return find_parent(parent, parent[node])


def connect_sets(parent, rank, node1, node2):
    """
    Функція об'єднання двох множин.

    Параметри:
    - parent: словник, представлення батьківських вершин
    - rank: словник, представлення рангів вершин
    - node1: рядок, вершина графа
    - node2: рядок, вершина графа

    Повертає:
    True, якщо множини були успішно об'єднані.
    False, якщо множини вже об'єднані.
    """
    root1 = find_parent(parent, node1)
    root2 = find_parent(parent, node2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1
        return True
    return False


def kruskal(graph):
    """
    Функція для знаходження мінімального кістякового дерева за допомогою алгоритму Крускала.

    Параметри:
    - graph: словник, представлення графа

    Повертає:
    Мінімальну вагу кістякового дерева.
    """
    edges = []
    for node1 in graph:
        for node2, distance in graph[node1].items():
            edges.append((distance, node1, node2))
    edges.sort()

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}
    total_distance = 0

    connected_nodes = 0
    for distance, node1, node2 in edges:
        if connect_sets(parent, rank, node1, node2):
            total_distance += distance
            connected_nodes += 1
    if connected_nodes == len(graph) - 1:
        return total_distance
    else:
        return -1


def minimum_fiber_length(filename):
    """
    Функція для знаходження мінімальної довжини кабелю.

    Параметри:
    - filename: рядок, назва CSV файлу

    Повертає:
    Мінімальну довжину оптоволоконного кабелю або -1, якщо не вдалося знайти зв'язаний граф
    """
    graph = read_graph_from_csv(filename)
    return kruskal(graph)


if __name__ == "__main__":
    filename = 'communication_wells.csv'
    print(minimum_fiber_length(filename))
