from auction import Auction, Auctioneer


def test_build_auction(make_params):
    auction = Auction()
    auction.make_params = make_params
    auction.make_graph()

    params = make_params()
    assert auction.nsellers() == params.nsellers
    assert auction.nbuyers() == params.nbuyers
    assert all(auction.nnodes('seller', buyer) >= 2 for buyer in auction.buyers())


def test_run_auction_round(make_params):
    auctioneer = Auctioneer()
    auctioneer.make_params = make_params
    auctioneer.make_graph()
    frame = auctioneer.run_auctions(0)

    assert not frame['nodes'].empty
    assert not frame['edges'].empty
    assert frame['nodes'].index.unique().tolist() == [0]
