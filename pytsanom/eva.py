from __future__ import division

import math

from objects import AnomalyDetector


class ZValueOfflineDetector(AnomalyDetector):

    @classmethod
    def detect(cls, data):
        mean = cls.compute_mean(data)
        std = cls.compute_standard_devation(data, mean)
        zscores = cls.compute_zscores(data, mean, std)
        return zscores

    @staticmethod
    def compute_mean(data):
        return sum(data) / len(data)

    @staticmethod
    def compute_standard_deviation(data, mean):
        total = 0
        for i in data:
            value = (i - mean)**2
            total = total + value

        total = total / len(data)
        total = math.sqrt(total)
        return total

    @staticmethod
    def compute_zscores(data, mean, std):
        values = []
        for i in data:
            zscore = (i - mean) / std
            values.append(zscore)
        return values
