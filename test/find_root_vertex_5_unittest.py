import unittest
from find_root_vertex_5 import bfs, find_root_vertex


class TestFindRootVertex(unittest.TestCase):
    def test_graph_with_root_vertex(self):
        edges = [(4, 5), (5, 0), (0, 1), (1, 2), (2, 3), (3, 0)]
        n = 6
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])

        self.assertEqual(find_root_vertex(graph, n), 4)

    def test_graph_without_root_vertex(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5)]
        n = 6
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])

        self.assertEqual(find_root_vertex(graph, n), -1)

    def test_empty_graph(self):
        graph = []
        n = 0
        self.assertEqual(find_root_vertex(graph, n), -1)


if __name__ == '__main__':
    unittest.main()
