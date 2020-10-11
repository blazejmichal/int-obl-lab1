from TaskA import TaskA
from TaskB import TaskB
from TaskC import TaskC
from TaskD import TaskD
from TaskE import TaskE

def run():
    TaskA.execute()
    TaskB.execute()
    TaskC.execute()
    taskD = TaskD()
    taskD.execute()
    taskE = TaskE()
    taskE.execute()

run()
