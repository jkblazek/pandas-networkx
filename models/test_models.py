from models import Node


def test_node_updates_graph(make_params):
    params = make_params()
    seller = Node(params.seller)
    buyer = Node(params.buyer)
    seller.add_node(buyer)

    buyer.price = 88.5

    assert buyer in seller
    assert seller._node['price'].iloc[0] == 88.5
