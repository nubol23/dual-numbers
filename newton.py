from dual_numbers.dual_numbers import Dual, DualArray
from typing import Callable, Union


def make_dual(function: Callable[[float], float]) -> Callable[[Dual], Dual]:
    def wrapper_accepting_arguments(x: Dual) -> Dual:
        return Dual(function(Dual(x)))
    return wrapper_accepting_arguments


@make_dual
def f(x): return x**3 - 4


def main():
    x = 0.1
    for i in range(300):
        res: Dual = f(x)
        x = x - res.real/res.deriv

    print(x.real, f(x).real)


if __name__ == '__main__':
    main()