"""Unit tests for hfs_fit.py."""
from hfs_fit.hfs_fit import (
    hfs
)

import matplotlib.pyplot as plt
from pytest import fixture


@fixture
def hfs_obj():
    """A example hfs_obj for tests."""
    return hfs('tests/sample_spectrum.txt', 'tests/fitLog.xlsx', nuclearSpin = 3.5)


def test_plot_spec(hfs_obj):
    """Check hfs.PlotSpec runs."""
    hfs_obj.PlotSpec()
    assert plt.gcf().get_axes(), 'a figure should have been plotted'
