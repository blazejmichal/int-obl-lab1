import numpy as np


class TaskG:

    def __init__(self):
        pass

    @classmethod
    def execute(cls, v):
        cls.normalizeVector(v)

    @classmethod
    def normalizeVector(cls, v):
        max = np.amax(v)
        min = np.amin(v)
        result = v.copy()
        for i in range(len(v)):
            result[i] = (v[i] - min) / (max - min)
        print('Znormalizowany wektor: ' + str(result))
        normalizedV = v / (np.linalg.norm(v))
        print('Znormalizowany przez numpy: ' + str(normalizedV))
