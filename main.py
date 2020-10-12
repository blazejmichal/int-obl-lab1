from TaskA import TaskA
from TaskB import TaskB
from TaskC import TaskC
from TaskD import TaskD
from TaskE import TaskE
from TaskF import TaskF
from TaskG import TaskG


def run():
    TaskA.execute()
    TaskB.execute()
    TaskC.execute()
    taskD = TaskD()
    taskD.execute()
    taskE = TaskE()
    v = taskE.execute()
    taskF = TaskF()
    taskF.execute(v)
    taskG = TaskG()
    taskG.execute(v)


run()
