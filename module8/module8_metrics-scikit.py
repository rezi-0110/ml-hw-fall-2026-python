"""Module 8: binary precision and recall with NumPy and scikit-learn.

AI Assistance Disclosure:
This program was prepared with the assistance of an AI tool (ChatGPT).
AI was used to help draft and review the code.
"""

import numpy as np
from sklearn.metrics import precision_score, recall_score


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Error: please enter a positive integer.")


def read_binary_label(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
        except ValueError:
            pass
        print("Error: please enter 0 or 1.")


def main():
    n = read_positive_integer("Enter N (number of points): ")
    points = np.empty((n, 2), dtype=int)

    for i in range(n):
        print(f"Point {i + 1} of {n}:")
        points[i, 0] = read_binary_label("  Enter x (correct label): ")
        points[i, 1] = read_binary_label("  Enter y (predicted label): ")

    correct = points[:, 0]
    predicted = points[:, 1]
    precision = precision_score(correct, predicted, pos_label=1, zero_division=0)
    recall = recall_score(correct, predicted, pos_label=1, zero_division=0)

    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    if not np.any(predicted == 1):
        print("Note: no predicted positives; undefined precision is reported as 0.")
    if not np.any(correct == 1):
        print("Note: no actual positives; undefined recall is reported as 0.")


if __name__ == "__main__":
    main()
