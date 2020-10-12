from random import randrange


class TaskE:
    a = []

    def __init__(self):
        i = 0
        while i < 50:
            self.a.append(randrange(10))
            i += 1

    def execute(self):
        print('Wektor ' + str(len(self.a)) + ' losowych: ' + str(self.a))
        return self.a
