from src.lib.data_loader import *


def test_shape():
    df = master()
    assert df.shape[0] == 3066
    assert df.shape[1] == 9
