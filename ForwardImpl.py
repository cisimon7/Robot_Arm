from numpy import set_printoptions
from sympy import trigsimp, lambdify
from utils import *

# Joint parameters declaration
q1, q2, q3, q4, q5 = symbols("q1 q2 q3 q4 q5", real=True)

# Guesses for link lengths
l1, l2, l3, l4, l5 = 1, 1, 1, 1, 1

# Forward Kinematics
H = Rx(q1)*Tx(l1)*Ry(q2)*Tz(l2)*Rz(q3)*Tz(l3)*Rx(q4)*Tz(l4)*Rz(q5)*Tz(l5)
H = trigsimp(H)

set_printoptions(suppress=True)


def forwardKinematics():
    return lambdify([(q1, q2, q3, q4, q5)], H, "numpy")
