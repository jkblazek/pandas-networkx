import numpy as np

from nxn import nxNode


class TestNode(nxNode):
    __test__ = False
    name = 0
    index = ['name']

    def __init__(self, name):
        self.name = name
        super().__init__(name=name)

    def __array__(self, dtype=None, copy=None):
        return np.array([self.name], dtype=dtype)


def test_add_nodes():
    graph = nxNode()
    node = TestNode(1)
    graph.add_node(node)
    graph.add_node(node)
    assert list(graph.nodes()) == [node]


def test_add_and_update_edge():
    graph = nxNode()
    source, target = TestNode(1), TestNode(2)
    graph.add_edge(source, target, ts=10)
    graph.add_edge(source, target, ts=12)

    assert list(graph.edges()) == [(1, 2)]
    assert graph[source].iloc[0]['ts'] == 12
