import random

import numpy as np
import pytest

from models import Node
from params import make_params as load_params


@pytest.fixture
def make_params(monkeypatch):
    monkeypatch.setattr(Node, 'name', 0)
    monkeypatch.setattr(Node, 'names', [])
    random.seed(42)
    np.random.seed(42)
    return load_params
