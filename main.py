import numpy as np

from dual_numbers.dual_numbers import Dual, exp, expm, DualArray


def sigmoid(x):
    """
    :param x: input value
    :return: Tuple[f(x), f'(x)]
    """
    res = 1/(1 + exp(-Dual(x)))
    return res.real, res.deriv


def main():
    np.set_printoptions(suppress=True)
    # print(sigmoid(3))

    # Gradiente
    # x = DualArray(1, [1, 0])
    # y = DualArray(2, [0, 1])
    # g = x ** 2 * y + x + y
    # print(g.real, g.deriv)

    # Jacobiano
    # ff = lambda xx, yy: [xx ** 2 + yy ** 2, xx + yy]
    # print(ff(x, y))

    # Mas gradientes
    # a = DualArray(1, [1, 0, 0])
    # b = DualArray(0.5, [0, 1, 0])
    # c = DualArray(2, [0, 0, 1])

    # d = c*(a+b)**2
    # print(d.real, d.deriv)

    # Otro gradiente
    x = DualArray(9, [1, 0, 0])
    y = DualArray(4, [0, 1, 0])
    z = DualArray(5, [0, 0, 1])
    g = 3*x**2 + y**2-x + expm(2*z)
    dx = 6*x.real - 1
    dy = 2*y.real
    dz = 2*np.exp(2*z.real)
    print(g.real)
    print(g.deriv.tolist())
    print([dx, dy, dz])

    # Otro jacobiano
    # gg = [3*x**2, y**2-1, expm(2*z)]
    # print(gg)


if __name__ == '__main__':
    main()
