"""Integration tests for the service as a whole."""

import os
from unittest.mock import patch

from numpy import testing
from hfs_fit import hfs


# @patch('hfs_fit.hfs_fit.get_user_levels')
# @patch('hfs_fit.hfs_fit.get_user_wavenumber')
# @patch('hfs_fit.hfs_fit.get_user_noise')
def test_hfs():
    """Run a full test of the script."""
    # setup
    # mock_user_levels.return_value = 2, 2
    # mock_user_noise.return_value = 37945, 37975
    # mock_user_wavenumber.return_value = 'z5S2', 'a5P2', 37978, 37980

    # run svc
    obj = hfs(
        'tests/sample_spectrum.txt',
        'tests/fitLog.xlsx',
        nuclearSpin = 3.5,
        upperJ=2,
        lowerJ=2,
        upperLabel='z5S2',
        lowerLabel='a5P2',
        noise_start_wn=37945,
        noise_end_wn=37975,
        start_wn=37978,
        end_wn=37980
    )
    obj.NewFit()
    obj.PlotGuess()
    obj.Optimise(2)

    # validate
    testing.assert_almost_equal(obj.SNR, 52.386236188012326)
    testing.assert_almost_equal(obj.normFactor, 3.90336975182)
    testing.assert_almost_equal(obj.relIntensities[0], 0.16923077)
    testing.assert_almost_equal(obj.relIntensities[-2], 0.26923077)
    testing.assert_almost_equal(obj.relIntensities[-1], 1.)
    testing.assert_almost_equal(obj.fitParams[0], -5.03268524e-02)
    testing.assert_almost_equal(obj.fitParams[-2], 3.79790274e+04, decimal=3)
