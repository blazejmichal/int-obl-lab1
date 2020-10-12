from random import randrange


class TaskF:

    def __init__(self):
        pass

    @classmethod
    def execute(cls, v):
        cls.calcAverage(v)

    @classmethod
    def calcAverage(cls, v):
        result = sum(v) / len(v)
        print('Średnia wektora: ' + str(result))
