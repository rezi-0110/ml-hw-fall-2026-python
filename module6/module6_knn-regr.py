"""One-dimensional k-nearest-neighbors regression using NumPy.

AI assistance disclosure:
This program was prepared with the assistance of an AI tool (ChatGPT).
AI was used to help draft and review the code.
"""

import numpy as np


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Error: please enter a positive integer.")


def read_real_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if np.isfinite(value):
                return value
        except ValueError:
            pass
        print("Error: please enter a finite real number.")


def knn_regression(points, query_x, k):
    """Return the mean y-value of the k closest x-values."""
    distances = np.abs(points[:, 0] - query_x)
    nearest_indices = np.argsort(distances, kind="stable")[:k]
    return float(np.mean(points[nearest_indices, 1]))


def main():
    n = read_positive_integer("Enter N (number of training points): ")
    k = read_positive_integer("Enter k (number of neighbors): ")

    points = np.empty((n, 2), dtype=float)
    for i in range(n):
        print(f"Point {i + 1} of {n}:")
        points[i, 0] = read_real_number("  Enter x: ")
        points[i, 1] = read_real_number("  Enter y: ")

    query_x = read_real_number("Enter X to predict Y: ")

    if k > n:
        print(f"Error: k ({k}) cannot be greater than N ({n}).")
        return

    prediction = knn_regression(points, query_x, k)
    print(f"Predicted Y: {prediction:g}")


if __name__ == "__main__":
    main()
