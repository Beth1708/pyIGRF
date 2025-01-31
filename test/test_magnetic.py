import pytest
import pyIGRF
import numpy as np

def test_pyigrf():
    # Test inputs
    lat = 40
    lon = 116
    alt = 300
    date = 1999

    # Expected outputs
    # Replace these placeholders with actual expected results
    expected_igrf_value = (np.float64(-5.080158216428891), np.float64(57.85556540804095),
                           np.float64(24750.880520185507), np.float64(24653.65386814849),
                           np.float64(-2191.6745821461395), np.float64(39388.393401984154),
                           np.float64(46519.368238551644))
    expected_igrf_variation = (np.float64(-0.02280011908546534), np.float64(0.040877153896800106),
                               np.float64(-19.857404366021854), np.float64(-20.6515490474103),
                               np.float64(-8.052244295431365), np.float64(30.777595502899203),
                               np.float64(15.494440798039147))
    expected_g_length = 14
    expected_h_length = 14

    # Assertions for function outputs
    igrf_value_result = pyIGRF.igrf_value(lat, lon, alt, date)
    assert igrf_value_result == expected_igrf_value, f"Unexpected igrf_value result: {igrf_value_result}"

    igrf_variation_result = pyIGRF.igrf_variation(lat, lon, alt, date)
    assert igrf_variation_result == expected_igrf_variation, f"Unexpected igrf_variation result: {igrf_variation_result}"

    # Assertions for coefficients
    g, h = pyIGRF.loadCoeffs.get_coeffs(date)
    assert len(g) == expected_g_length, f"Unexpected number of g coefficients: {len(g)}"
    assert len(h) == expected_h_length, f"Unexpected number of h coefficients: {len(h)}"