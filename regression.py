from sklearn.datasets import make_classification
import numpy as np
from dual_numbers.dual_numbers import expm, DualArray


def sigmoid(x):
    """
    :param x: input value
    :return: Tuple[f(x), f'(x)]
    """
    res = 1/(1 + expm(-DualArray(x, 1)))
    return res.real, res.deriv


def main():
    X, Y = make_classification(n_samples=20, n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)
    X = (X - np.mean(X, axis=0, keepdims=True)) / np.std(X, axis=0, keepdims=True)

    phi_x = np.hstack((np.ones((len(X), 1)), X))
    theta = np.random.randn(3, 1)
    z = phi_x @ theta

    res = sigmoid(z)
    print(res[0])
    print()
    print(res[1])

    # y_hat, y_deriv = sigmoid(z)
    #
    # correct_deriv = 1/len(phi_x)*phi_x.T@(y_hat - Y[:, np.newaxis])


if __name__ == '__main__':
    main()