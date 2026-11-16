"""Module 7: k-NN regression with NumPy and scikit-learn.

AI Assistance Disclosure:
This program was prepared with the assistance of an AI tool (ChatGPT).
AI was used to help draft and review the code.
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor


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


def main():
    n = read_positive_integer("Enter N (number of training points): ")
    k = read_positive_integer("Enter k (number of neighbors): ")

    points = np.empty((n, 2), dtype=float)
    for i in range(n):
        print(f"Point {i + 1} of {n}:")
        points[i, 0] = read_real_number("  Enter x: ")
        points[i, 1] = read_real_number("  Enter y: ")

    query_x = read_real_number("Enter X to predict Y: ")

    labels = points[:, 1]
    variance = np.var(labels)  # Population variance (ddof=0).
    print(f"Variance of training labels: {variance:g}")

    if k > n:
        print(f"Error: k ({k}) cannot be greater than N ({n}).")
        return

    model = KNeighborsRegressor(n_neighbors=k, weights="uniform", metric="euclidean")
    model.fit(points[:, 0].reshape(-1, 1), labels)
    prediction = model.predict(np.array([[query_x]], dtype=float))[0]
    print(f"Predicted Y: {prediction:g}")


if __name__ == "__main__":
    main()
