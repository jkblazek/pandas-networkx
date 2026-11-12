import sys
import time
from threading import Thread

from dash import Dash, Input, Output, dcc, html

from params import make_params
from sim import MarketSim


app = Dash(__name__)
sim = MarketSim(make_params)
fig = sim.fig
auction_round = 1

app.layout = html.Div([
    dcc.Graph(id='price', figure=fig),
    dcc.Interval(id='refresh', interval=1000),
])


@app.callback(Output('price', 'figure'), Input('refresh', 'n_intervals'))
def refresh_figure(_):
    return fig


def do_round():
    global fig, auction_round
    fig = sim.do_round(auction_round)
    sim.print_round(auction_round)
    auction_round += 1
    return fig


def run_simulation():
    while True:
        do_round()
        time.sleep(0.1)


if __name__ == '__main__':
    if '--dashboard' in sys.argv:
        Thread(target=run_simulation, daemon=True).start()
        app.run()
    else:
        try:
            run_simulation()
        except KeyboardInterrupt:
            pass
