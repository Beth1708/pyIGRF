import pyIGRF

if __name__ == '__main__':
    lat = 40
    lon = 116
    alt = 300
    date = 1999
    print("igrf_value and igrf_variation docstrings:")
    print(pyIGRF.igrf_value.__doc__)
    print()
    print(pyIGRF.igrf_variation.__doc__)
    print("igrf_value and igrf_variation results for lat = 40, lon = 116, alt = 300, date = 1999")
    igrf_value_result = pyIGRF.igrf_value(lat, lon, alt, date)
    print(igrf_value_result)
    print("igrf_variation results for lat = 40, lon = 116, alt = 300, date = 1999")
    igrf_variation_result = pyIGRF.igrf_variation(lat, lon, alt, date)
    print(igrf_variation_result)
    print("g and h coefficients lengths:")
    g, h = pyIGRF.loadCoeffs.get_coeffs(date)
    print(len(g))
    print(len(h))
