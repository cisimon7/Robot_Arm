from ForwardImpl import forwardKinematics
from math import pi
from numpy import round


def forward_tests():
    # test cases
    # you can add more test cases here
    # angles input should be in degrees
    test_cases = [
        # q1, q2, q3, q4, q5
        [0, 0, 0, 0, 0],
        [30, 50, 20, 10, 20]
    ]

    f_function = forwardKinematics()

    for i, param in enumerate(test_cases):
        h = f_function((
            (param[0] * (pi/180)),  # q1
            (param[1] * (pi/180)),  # q2
            param[2],  # a2
            param[3],  # d1
            param[4]   # d3
        ))

        view = f"CASE {i + 1}:\n{round(h, 4)}\n"
        print(view)


if __name__ == '__main__':
    forward_tests()
