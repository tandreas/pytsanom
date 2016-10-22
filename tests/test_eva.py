from pytsanom.eva import ZValueOfflineDetector


def test_eva_zscore_on2_mean():
    test_data = [5, 10, 30, 55, 19, 16, 83]
    mean = ZValueOfflineDetector.compute_mean(test_data)
    mean = round(mean, 4)
    assert mean == 31.1429


def test_eva_zscore_on2_std():
    test_data = [5, 10, 30, 55, 19, 16, 83]
    mean = ZValueOfflineDetector.compute_mean(test_data)
    std = ZValueOfflineDetector.compute_standard_deviation(test_data, mean)
    std = round(std, 4)
    assert std == 26.0956


def test_eva_zscore_on2_zscore():
    test_data = [5, 10, 30, 55, 19, 16, 83]
    mean = ZValueOfflineDetector.compute_mean(test_data)
    std = ZValueOfflineDetector.compute_standard_deviation(test_data, mean)
    zscores = ZValueOfflineDetector.compute_zscores(test_data, mean, std)
    zscores = [round(v, 4) for v in zscores]
    expected = [-1.0018, -0.8102, -0.0438, 0.9142, -0.4653, -0.5803, 1.9872]
    assert zscores == expected
