from __future__ import annotations

from typing import Union, Iterable
import numpy as np


class Dual:
    def __init__(self, a: Union[int, float, Dual] = 0, b: Union[int, float] = 1):
        if isinstance(a, Dual):
            self.real = a.real
            self.deriv = a.deriv
        else:
            if not (isinstance(a, (int, float)) or isinstance(b, (int, float))):
                raise ValueError('Invalid parameters')
            self.real = a
            self.deriv = b

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.deriv + other.deriv)
        elif isinstance(other, (int, float)):
            return Dual(self.real + other, self.deriv)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.deriv - other.deriv)
        elif isinstance(other, (int, float)):
            return Dual(self.real - other, self.deriv)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real*other.real, self.real*other.deriv + other.real*self.deriv)
        elif isinstance(other, (int, float)):
            return Dual(self.real*other, self.deriv*other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real/other.real, (self.deriv*other.real - self.real*other.deriv)/(other.real**2))
        elif isinstance(other, (int, float)):
            return Dual(self.real/other, self.deriv/other)

    def __rtruediv__(self, other):
        if isinstance(other, Dual):
            return Dual(other.real / self.real, (other.deriv * self.real - other.real * self.deriv) / (self.real ** 2))
        elif isinstance(other, (int, float)):
            return Dual(other / self.real, (-other*self.deriv)/self.real**2)

    def __floordiv__(self, other):
        if isinstance(other, Dual):
            return Dual(int(self.real / other.real), int((self.deriv * other.real - self.real * other.deriv) / (other.real ** 2)))
        elif isinstance(other, (int, float)):
            return Dual(int(self.real/other), int(self.deriv/other))

    def __rfloordiv__(self, other):
        if isinstance(other, Dual):
            return Dual(int(other.real / self.real), int((other.deriv * self.real - other.real * self.deriv) / (self.real ** 2)))
        elif isinstance(other, (int, float)):
            return Dual(int(other / self.real), int((-other * self.deriv) / self.real ** 2))

    def __neg__(self):
        return Dual(-self.real, -self.deriv)

    def __pow__(self, power, modulo=None):
        return Dual(self.real**power, power*self.real**(power-1)*self.deriv)

    def __str__(self) -> str:
        if self.deriv >= 0:
            return f'{self.real:.4f} + {self.deriv:.4f}ε'
        else:
            return f'{self.real:.4f}'


def exp(x: Union[int, float, Dual]):
    if not isinstance(x, Dual):
        x = Dual(x)
    return Dual(np.exp(x.real), x.deriv * np.exp(x.real))


def expm(x: Union[int, float, Dual]):
    return DualArray(np.exp(x.real), x.deriv * np.exp(x.real))


class DualArray:
    def __init__(self, a: Union[Iterable, int, float], b: Union[Iterable, int, float]):
        self.real = np.asarray(a)
        self.deriv = np.asarray(b)

    def __add__(self, other):
        if isinstance(other, DualArray):
            return DualArray(self.real + other.real, self.deriv + other.deriv)
        else:
            return DualArray(self.real + other, self.deriv)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, DualArray):
            return DualArray(self.real - other.real, self.deriv - other.deriv)
        elif isinstance(other, (int, float)):
            return DualArray(self.real - other, self.deriv)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __neg__(self):
        return DualArray(-self.real, -self.deriv)

    def __mul__(self, other):
        if isinstance(other, DualArray):
            return DualArray(self.real * other.real, self.real * other.deriv + other.real * self.deriv)
        elif isinstance(other, (int, float)):
            return DualArray(self.real * other, self.deriv * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, DualArray):
            return DualArray(self.real / other.real, (self.deriv * other.real - self.real * other.deriv) / (other.real ** 2))
        elif isinstance(other, (int, float)):
            return DualArray(self.real / other, self.deriv / other)

    def __rtruediv__(self, other):
        if isinstance(other, DualArray):
            return DualArray(other.real / self.real, (other.deriv * self.real - other.real * self.deriv) / (self.real ** 2))
        elif isinstance(other, (int, float)):
            return DualArray(other / self.real, (-other * self.deriv) / self.real ** 2)

    def __pow__(self, power, modulo=None):
        return DualArray(self.real ** power, power * self.real ** (power - 1) * self.deriv)

    def __matmul__(self, other):
        return DualArray(self.real.dot(other.real), self.deriv.dot(other.real) + self.real.dot(other.deriv))

    def __rmatmul__(self, other):
        return self @ other

    # def __str__(self) -> str:
    #     if np.count_nonzero(self.deriv) >= 0:
    #         return f'{self.real} + {self.deriv}ε'
    #     else:
    #         return f'{self.real}'

    def __str__(self) -> str:
        return str(self.real)

    def __repr__(self):
        if np.count_nonzero(self.deriv) >= 0:
            return f'{self.real}, {self.deriv}ε'
        else:
            return f'{self.real}'
