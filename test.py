from itertools import count

from params import make_params
from sim import MarketSim


if __name__ == '__main__':
    sim = MarketSim(make_params)
    for round_number in count(1):
        sim.do_round(round_number)
        sim.print_round(round_number)
