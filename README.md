# pandas-networkx

An experimental market simulator that stores auction participants and graph edges in pandas. Buyers and sellers update bids and prices each round. The auctioneer records snapshots for the Plotly visualization.

## Setup

Install Python 3.12, 3.13, or 3.14 and Poetry 2. NetworkX excludes Python 3.14.1, so use another patch release if you choose 3.14.

```sh
poetry sync
poetry run python -m pytest
```

## Run the simulator

Run the simulation in the terminal until you stop it with Ctrl+C.

```sh
poetry run python app.py
```

For the Dash view, pass `--dashboard` and open the local URL printed by Dash.

```sh
poetry run python app.py --dashboard
```

Edit `params/params.dat` before running to change the number of buyers (`nbuyers`), sellers (`nsellers`), and other simulation settings. In an interactive Python session, `MarketSim(make_params)` runs the initial round, and `sim.do_round(1)` advances the simulation and returns the Plotly figure.
