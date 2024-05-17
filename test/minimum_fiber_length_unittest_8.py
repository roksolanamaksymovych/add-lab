import unittest
from minimum_fiber_length_8 import read_graph_from_csv, kruskal, minimum_fiber_length

class TestMinimumFiberLength(unittest.TestCase):

    def test_read_graph_from_csv(self):
        filename = 'communication_wells.csv'
        graph = read_graph_from_csv(filename)
        expected_graph = {'K1': {'K2': 2000, 'K3': 1500}, 'K2': {'K1': 2000, 'K3': 1000}, 'K3': {'K1': 1500, 'K2': 1000}}
        self.assertEqual(graph, expected_graph)

    def test_kruskal(self):
        filename = 'communication_wells.csv'
        graph = read_graph_from_csv(filename)
        min_spanning_tree = kruskal(graph)
        expected_min_spanning_tree = 2500
        self.assertEqual(min_spanning_tree, expected_min_spanning_tree)

    def test_minimum_fiber_length(self):
        filename = 'communication_wells.csv'
        result = minimum_fiber_length(filename)
        expected_result = 2500
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
