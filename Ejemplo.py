from sr2 import *
import random

glInit()
glCreateWindow(100, 100)
glViewPort(0, 0, 100, 100)
glClearColor(1, 1, 1)
glClear()
glColor(1, 1, 1)
x = random.uniform(-1, 1)
y = random.uniform(-1, 1)
glLine(-1, -1, 1, 0)
glFinish()
