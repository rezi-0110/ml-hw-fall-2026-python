"""Prepared with assistance from an AI agent."""

from module5.module5_mod import NumberCollection


def main():
    n = int(input("Enter N: "))
    collection = NumberCollection()

    for i in range(n):
        collection.add_number(int(input(f"Enter number {i + 1}: ")))

    x = int(input("Enter X: "))
    print(collection.search(x))


if __name__ == "__main__":
    main()
