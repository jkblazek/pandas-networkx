from sim import MarketSim


def test_simulation_adds_plot_frames(make_params):
    sim = MarketSim(make_params)
    for round_number in range(1, 4):
        sim.do_round(round_number)

    assert sim.node_history.index.unique().tolist() == [0, 1, 2, 3]
    assert [frame.name for frame in sim.fig.frames] == ['1', '2', '3']
