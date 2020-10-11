class TaskB:
    a = [3, 8, 9, 10, 12]
    b = [8, 7, 7, 5, 6]

    @staticmethod
    def execute():
        TaskB.addVectors()
        TaskB.multiplyVectors()

    @staticmethod
    def addVectors():
        result = []
        for i in range(len(TaskB.a)):
           result.append(TaskB.a[i] + TaskB.b[i])
        print('Suma wektorów: ' + str(result))


    @staticmethod
    def multiplyVectors():
        result = []
        for i in range(len(TaskB.a)):
           result.append(TaskB.a[i] * TaskB.b[i])
        print('Iloczyn wektorów: ' + str(result))