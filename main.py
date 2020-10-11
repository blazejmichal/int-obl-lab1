from TaskA import TaskA
from TaskB import TaskB
from TaskC import TaskC
from TaskD import TaskD

def run():
    TaskA.execute()
    TaskB.execute()
    TaskC.execute()
    taskD = TaskD()
    taskD.execute()

run()
