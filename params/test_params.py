def test_population_matches_parameters(make_params):
    params = make_params()
    assert params.nnodes == params.nbuyers + params.nsellers
    assert params.g_max >= 2
